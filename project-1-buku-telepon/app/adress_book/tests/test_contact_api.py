"""
Test contact APIs.
"""

from django.test import TestCase
from rest_framework.test import APIClient

from core import models

class TestContactAPI(TestCase):
    """
    Test contact API requests.
    """
    
    def setUp(self):
        self.client = APIClient()
    