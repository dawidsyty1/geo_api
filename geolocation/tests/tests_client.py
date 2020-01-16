# Create your tests here.
from django.test import TestCase
from geolocation import client
from unittest.mock import patch


class ClientTests(TestCase):
    data = {
        "value": "http://www.google.com",
        "type": "url"
    }

    def test_remove_url_schema(self):
        """Remove url schema"""

        field = client.remove_url_schema(self.data)
        self.assertEqual("www.google.com", field["value"])

    @patch("ipstack.GeoLookup.get_location", return_value={"type": None})
    def test_get_geolookup_data_raises_exception(self, get_location):
        """Incorect data from external server"""
        with self.assertRaises(client.GeolocationClientError):
            client.get_geolookup_data(self.data)

    def test_get_geolookup_data_success(self):
        """Successed getting data from host """
        response = client.get_geolookup_data(self.data)
        self.assertEqual(response['url'], "www.google.com")
