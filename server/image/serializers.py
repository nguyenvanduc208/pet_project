from rest_framework import serializers
from image.models import Image

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Image
        fields = ('id', 'title', 'path')