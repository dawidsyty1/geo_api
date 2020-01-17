from django.test import TestCase
from geolocation import validators
from rest_framework import serializers
from django.core import exceptions


class ValidatorsTests(TestCase):

    def test_validate_ip4_address_invalid(self):
        with self.assertRaises(serializers.ValidationError):
            validators.validate_ip_address("1233.33x3222.22")

    @staticmethod
    def test_validate_ip4_address_valid():
        validators.validate_ip_address("192.145.12.12")

    @staticmethod
    def test_validate_ip6_address_invalid():
        validators.validate_ip_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

    @staticmethod
    def test_validate_url_address_valid():
        validators.validate_url_address("www.google.com")

    def test_validate_url_address_invalid(self):
        with self.assertRaises(exceptions.ValidationError):
            validators.validate_url_address("google")
