from django.core.validators import URLValidator
from django.core.validators import validate_ipv4_address, validate_ipv6_address
from rest_framework import serializers


class CustomURLValidator(URLValidator):
    """Custom URL validator."""

    def __call__(self, value):
        if '://' not in value:
            value = 'https://' + value
        super(CustomURLValidator, self).__call__(value)


def validate_url_address(url):
    """The method validating URL"""
    validate = CustomURLValidator()
    validate(url)


def validate_ip_address(value):
    """The method validating ipv4 and ipv6 address"""

    error_message = None
    try:
        validate_ipv4_address(value)
    except Exception as error:
        error_message = error
    if error_message:
        try:
            validate_ipv6_address(value)
        except Exception as error:
            raise serializers.ValidationError("{} or {}".format(error, error_message))
