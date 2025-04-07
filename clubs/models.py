from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

class Club(TimeStampedModel):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="club_members", blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='clubs/icons', blank=True, null=True)
    

    def __str__(self):
        return self.name
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
        ]
