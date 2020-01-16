import logging
from rest_framework import serializers
from geolocation.models import GeolocationData
from geolocation import tasks, validators


class GeolocationsDataListSerializer(serializers.ModelSerializer):
    """ Serializer for the GeolocationData objects list"""

    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
    ip = serializers.CharField(required=False, validators=[validators.validate_ip_address])
    url = serializers.CharField(required=False, validators=[validators.validate_url_address])

    class Meta:
        model = GeolocationData
        fields = '__all__'


class GeolocationDataSerializer(serializers.ModelSerializer):
    """ Serializer for the GeolocationData objects"""
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
    ip = serializers.CharField(required=False, validators=[validators.validate_ip_address])
    url = serializers.CharField(required=False, validators=[validators.validate_url_address])

    class Meta:
        model = GeolocationData
        fields = (
            'ip', 'url'
        )

    def create(self, validated_data):
        data = self.data_from_fields(validated_data)
        tasks.add_or_update_geolocation_data(data)
        return validated_data

    def data_from_fields(self, data):
        for item in self.fields:
            if item in data:
                return {'value': data[item], 'type': item}
        raise serializers.ValidationError("Missing or incorrect data")
