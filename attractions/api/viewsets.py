from rest_framework.viewsets import  ModelViewSet
from attractions.models import Attraction
from .serializers import AttractionSerializer

class AttractionsViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer