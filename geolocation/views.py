# Create your views here.
from geolocation.models import GeolocationData
from geolocation.serializers import GeolocationsDataListSerializer, GeolocationDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins


class GeolocationDataView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    queryset = GeolocationData.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GeolocationsDataListSerializer
        return GeolocationDataSerializer
