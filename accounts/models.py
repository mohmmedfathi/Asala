from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    joined_communities = models.ManyToManyField("communities.Community", blank=True)
    joined_clubs = models.ManyToManyField("clubs.Club", blank=True)
    purchased_products = models.ManyToManyField("products.Product", related_name="buyers", blank=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]