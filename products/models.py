from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    # likes = models.ManyToManyField(CustomUser, related_name="liked_products", blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_products", blank=True)

    def __str__(self):
        return self.name
