from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from reviews.models import Review
from reviews.api.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
