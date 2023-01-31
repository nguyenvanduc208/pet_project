from django.shortcuts import render
from .models import Gallery
from rest_framework.views import APIView
from .serializers import GallerySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class GalleryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, product_id):
        gallery = Gallery.objects.filter(product=product_id)
        serializer = GallerySerializer(gallery, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = GallerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
