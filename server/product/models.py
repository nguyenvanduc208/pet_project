from django.db import models
from category.models import Category
from image.models import Image
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    star = models.IntegerField(default=0)
    title = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=1)
    amount = models.IntegerField()
    cate = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(to=Image, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'