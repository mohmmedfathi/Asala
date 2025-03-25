from django.db import models
from django.conf import settings
from category.models import Category
from model_utils.models import TimeStampedModel
    
class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_products", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
   
    def __str__(self):
        return self.name
