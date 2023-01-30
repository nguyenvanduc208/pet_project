from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=150)
    path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'