# from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from tourist_spots_core.models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'address__line1']
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return TouristSpot.objects.filter(approved=True)
        # id = self.request.query_params.get('id', None)
        # name = self.request.query_params.get('name', None)
        # description = self.request.query_params.get('description', None)
        # queryset = TouristSpot.objects.all()
        #
        # if id:
        #     queryset = TouristSpot.objects.filter(pk=id)
        # if name:
        #     queryset = queryset.filter(name__iexact=name)
        # if description:
        #     queryset = queryset.filter(description__iexact=description)
        #
        # return queryset

    def list(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # return Response({'message': f'Olá  {request.data["name"]}'})
        return super(TouristSpotViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).partial_update(request, *args, **kwargs)

    # @action(methods=['get'], detail=True)
    # def report(self, request, pk=None):
    #     pass
    #
    # @action(methods=['get'], detail=False)
    # def test(self, request):
    #     pass