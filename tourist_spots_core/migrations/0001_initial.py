# Generated by Django 3.1.1 on 2020-10-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('attractions', models.ManyToManyField(to='attractions.Attraction')),
                ('comments', models.ManyToManyField(to='comments.Comment')),
            ],
        ),
    ]
