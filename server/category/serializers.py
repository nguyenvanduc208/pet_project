from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image_path = serializers.CharField(source='image.path', allow_null=True)
    class Meta:
        model = Category
        fields = '__all__'