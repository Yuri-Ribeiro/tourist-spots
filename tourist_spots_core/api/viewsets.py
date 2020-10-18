# from rest_framework.response import Response
from rest_framework.decorators import action
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

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    @action(methods=['get'], detail=True)
    def report(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def test(self, request):
        pass