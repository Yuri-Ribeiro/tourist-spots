# Generated by Django 3.1.1 on 2020-10-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tourist_spots'),
        ),
    ]
