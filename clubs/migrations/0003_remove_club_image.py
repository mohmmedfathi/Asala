# Generated by Django 4.2.7 on 2025-03-26 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_club_clubs_club_id_78da8b_idx_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='image',
        ),
    ]
