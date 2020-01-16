from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User


class AccountsTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            email='user@foo.com',
            password='pass'
        )
        self.user.is_active = False
        self.user.save()

    def test_obtain_jwt_bad_request(self):
        # create an inactive user

        resp = self.client.post(
            "/api/v1/accounts/obtain_token",
            {'email': 'user@foo.com', 'password': 'pass'},
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtain_jwt_bad_request(self):
        # set the user to active and attempt to get a token from login
        self.user.is_active = True
        self.user.save()
        resp = self.client.post(
            "/api/v1/accounts/obtain_token",
            {'username': 'user', 'password': 'pass'},
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)

