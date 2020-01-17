# Create your models here.
import logging
from django.db import models


class GeolocationData(models.Model):
    IP_TYPES = (
        ('ipv4', 'ipv4'),
        ('ipv6', 'ipv6'),
    )
    url = models.URLField(default='')
    ip = models.GenericIPAddressField(default='192.168.0.1')
    type = models.CharField(max_length=4, choices=IP_TYPES)
    continent_code = models.CharField(max_length=2, default='')
    continent_name = models.CharField(max_length=50, default='')
    country_code = models.CharField(max_length=2, default='')
    country_name = models.CharField(max_length=50, default='')
    region_code = models.CharField(max_length=50, default='')
    region_name = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    zip = models.CharField(max_length=50, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def validate_fields(self, response):
        """
        Validate fields before the update.
        """
        response = {
            field.name: response.get(field.name)
            for field in self._meta.get_fields() if response.get(field.name) is not None
        }
        return response

    def update_from_dict(self, dictionary):
        """
        Updating model from dictionary.
        """
        self.__dict__.update(dictionary)
