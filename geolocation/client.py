from app import settings
from ipstack import GeoLookup
from rest_framework import exceptions

geolookup_client = GeoLookup(settings.IPSTACK_PRIVATE_KEY)


class GeolocationClientError(exceptions.APIException):
    pass


def remove_url_schema(field):
    """Remove from URL address doesn't necessary by GeoLookups library, schema."""
    if 'url' == field['type']:
        if "://" in field['value']:
            field['value'] = field['value'].split("://")[1]
    return field


def get_geolookup_data(field):
    """Make call to the external API service."""
    geolookup_client.find_hostname()

    field = remove_url_schema(field)

    # import pdb; pdb.set_trace()

    response = geolookup_client.get_location(field['value'])

    if not response or response['type'] is None:
        raise GeolocationClientError("An error occurred during getting location data from the server.")

    response[field['type']] = field['value']
    return response
