from django.db import models
from django.conf import settings

class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='clubs/', default='default.jpeg')

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="club_members", blank=True)

    def __str__(self):
        return self.name
