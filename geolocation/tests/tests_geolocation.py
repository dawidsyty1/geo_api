from django.test import TestCase
from rest_framework.test import APIClient
from geolocation import models, serializers
from unittest.mock import patch


class GeolocationApiTests(TestCase):
    fixtures = [
        'geolocation_data.json'
    ]

    def setUp(self):
        self.client = APIClient()

    @patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True)
    def test_retrieving_geolocation_data(self, authenticated):
        """Test retrieving GeolocationData"""
        geolocations_count = models.GeolocationData.objects.all().count()
        response = self.client.get('/api/v1/geolocation/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(geolocations_count, len(response.data))

    @patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True)
    def test_get_by_id_geolocation_data(self, authenticated):
        """Test get by id  GeolocationData"""
        objects = models.GeolocationData.objects.all().first()
        response = self.client.get('/api/v1/geolocation/{}/'.format(int(objects.id)), format='json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(objects.id, response.data['id'])

    @patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True)
    def test_create_geolocation_data_valid_url(self, authenticated):
        """Test creating GeolocationData with valid url address"""
        response = self.client.post('/api/v1/geolocation/', {"url": "www.google.com"}, format='json')
        self.assertEqual(201, response.status_code)

    @patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True)
    def test_create_geolocation_data_invalid_url(self, authenticated):
        """Test creating GeolocationData with invalid url address"""
        response = self.client.post('/api/v1/geolocation/', {"url": "google"}, format='json')
        self.assertEqual(400, response.status_code)

    @patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True)
    def test_geolocation_data_serializer(self, authenticated):
        """Test validating GeolocationDataListSerializer"""
        objects = models.GeolocationData.objects.all().first()
        response = self.client.get('/api/v1/geolocation/{}/'.format(int(objects.id)), format='json')
        serializer = serializers.GeolocationsDataListSerializer(objects)
        self.assertEqual(response.data['url'], serializer.data['url'])

    def test_get_data_without_authentication(self):
        """Test checking JWT authorization"""
        objects = models.GeolocationData.objects.all().first()
        response = self.client.get('/api/v1/geolocation/{}/'.format(int(objects.id)), format='json')
        self.assertEqual(401, response.status_code)
