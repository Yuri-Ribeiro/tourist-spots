# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from tourist_spots_core.models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        return TouristSpot.objects.filter(approved=True)

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 321})

    # def create(self, request, *args, **kwargs):
    #     return Response({'message': f'Olá  {request.data["name"]}'})

    # def destroy(self, request, *args, **kwargs):
    #     pass