from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

class Community(TimeStampedModel):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="community_members", blank=True)

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='communities/', default='default.jpeg')
    # created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
