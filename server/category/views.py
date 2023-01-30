from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer
from rest_framework.response import Response
from .models import Category
from rest_framework import pagination
from django.core.paginator import Paginator
# Create your views here.

class CategoryView(APIView):
    def get(self, request):
        page = request.GET.get('page')
        print('>>>>>>>>>>>>>>>>>>>>>',page)
        if page is None:
            page = 1

        data = Category.objects.all()
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
