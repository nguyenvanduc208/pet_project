from .serializers import CategorySerializer
from .models import Category

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.core.paginator import Paginator
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

# Create your views here.


class CategoryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_obj(self, pk):
        category = get_object_or_404(Category, pk=pk)
        return category

    def get(self, request, pk=None):
        if pk is not None:
            category = self.get_obj(pk)
            seralizer = CategorySerializer(category, many=False)
            return Response(seralizer.data)

        page = request.GET.get('page')
        data = Category.objects.all()
        if page is None:
            page_obj = data
        else:
            paginator = Paginator(data, 10)
            try:
                page_obj = paginator.page(page)
            except:
                return Response([])

        seralizer = CategorySerializer(page_obj, many=True)
        return Response(seralizer.data)

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_obj(pk)
        serializer = CategorySerializer(
            category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({'detail': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
        category = self.get_obj(pk)
        category.delete()

        return Response({'message': 'The object has been deleted successfully'}, status=status.HTTP_200_OK)
