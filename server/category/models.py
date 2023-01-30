from django.db import models
from image.models import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=1)
    image = models.ForeignKey(to=Image, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'categories'