# Generated by Django 3.1.1 on 2020-10-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('tourist_spots_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='reviews',
            field=models.ManyToManyField(to='reviews.Review'),
        ),
    ]
