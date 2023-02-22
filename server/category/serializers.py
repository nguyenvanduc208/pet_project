from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image_path = serializers.CharField(source='image.path', allow_null=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class InfoSerializer(serializers.Serializer):
    total_page = serializers.IntegerField()
    page = serializers.CharField()


class CustomSerializer(serializers.Serializer):
    result = CategorySerializer(many=True)
    info = InfoSerializer()