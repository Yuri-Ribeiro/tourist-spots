from rest_framework.serializers import ModelSerializer
from tourist_spots_core.models import TouristSpot
from attractions.api.serializers import AttractionSerializer
from addresses.api.serializers import AddressSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True, read_only=True)
    address = AddressSerializer()
    comments = CommentSerializer(many=True)
    reviews = ReviewSerializer(many=True)


    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'approved', 'photo',
                  'attractions', 'comments', 'reviews', 'address')