from django.db import models
from model_utils.models import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='category/icons', blank=True, null=True)
    
    def __str__(self):
        return self.name