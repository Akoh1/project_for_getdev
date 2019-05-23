from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.


# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.book_data = {'book': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create_book'),
            self.book_data,
            format="json")

    def test_api_can_create_a_book(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

