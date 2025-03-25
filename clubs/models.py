from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

class Club(TimeStampedModel):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="club_members", blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='clubs/', default='default.jpeg')
    icon = models.ImageField(upload_to='clubs/icons', blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
