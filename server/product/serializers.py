from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(source='cate.name', read_only=True)
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'star', 'title', 'description', 'status', 'amount', 'cate', 'category_name', 'image')
        extra_kwargs = {'cate': {'write_only': True}}
