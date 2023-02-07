from .serializers import CategorySerializer, CustomSerializer
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
            serializer = CategorySerializer(category, many=False)
            return Response(serializer.data)
        
        is_page = request.GET.get('page')
        categories = Category.objects.all()
        if is_page is None: 
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

        paginate = Paginator(categories, 10)
        page_data = paginate.page(is_page)

        page_info = {
            'total_page': paginate.__dict__['num_pages'],
            'page': is_page
        }

        serializer = CustomSerializer({
            'result': page_data,
            'info': page_info
        })

        return Response(serializer.data)

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
