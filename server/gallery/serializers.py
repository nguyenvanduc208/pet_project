from rest_framework import serializers
from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    image_path = serializers.CharField(source='image.path', read_only=True)
    class Meta:
        model = Gallery
        fields = ('image_path', 'image', 'product')
        extra_kwargs = {'image': {'write_only': True}}