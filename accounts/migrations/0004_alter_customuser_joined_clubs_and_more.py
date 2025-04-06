# Generated by Django 4.2.7 on 2025-04-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_remove_club_image'),
        ('communities', '0001_initial'),
        ('accounts', '0003_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='joined_clubs',
            field=models.ManyToManyField(blank=True, to='clubs.club'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='joined_communities',
            field=models.ManyToManyField(blank=True, to='communities.community'),
        ),
    ]
