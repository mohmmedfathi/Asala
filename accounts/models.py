from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product
from communities.models import Community
from clubs.models import Club

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    joined_communities = models.ManyToManyField(Community, related_name="user_communities", blank=True)
    joined_clubs = models.ManyToManyField(Club, related_name="user_clubs", blank=True)
    purchased_products = models.ManyToManyField(Product, related_name="buyers", blank=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username
