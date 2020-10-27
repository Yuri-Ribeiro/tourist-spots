from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from reviews.models import Review
from addresses.models import Address

class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='tourist_spots', null=True, blank=True)

    @property
    def complete_description2(self):
        return '%s - %s' %(self.name, self.description)

    def __str__(self):
        return self.name