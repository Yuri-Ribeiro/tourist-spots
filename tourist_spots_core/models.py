from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from reviews.models import Review

class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.name