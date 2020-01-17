from django.test import TestCase
from geolocation import tasks, models


class TaskTests(TestCase):
    request_data = {
        "value": "http://www.google.com",
        "type": "url"
    }

    def test_add_or_update_geolocation_data(self):
        """Get from external host and save geolocation data in database"""
        tasks.add_or_update_geolocation_data(self.request_data)
        count = models.GeolocationData.objects.all().count()
        self.assertEqual(count, 1)
