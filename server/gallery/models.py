from django.db import models
from image.models import Image
from product.models import Product

# Create your models here.
class Gallery(models.Model):
    image = models.ForeignKey(to=Image, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)


    class Meta:
        db_table = 'gallery'