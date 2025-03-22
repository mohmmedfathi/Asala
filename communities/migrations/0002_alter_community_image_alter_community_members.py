# Generated by Django 5.1.7 on 2025-03-22 10:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='communities/'),
        ),
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='community_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
