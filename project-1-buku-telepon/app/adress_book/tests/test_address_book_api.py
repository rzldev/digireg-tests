"""
Test address book APIs.
"""

import random

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core import models

ADDRESS_BOOK_URL = reverse('address-book:contact-list')

def create_contact(name):
    """
    Create and return a sample contact.
    """
    default = {
        'name': name,
        'telephone': '+62' + random.randint(1000000000, 10000000000)
    }
    contact = models.Contact.objects.create(**default)
    return contact

class TestAddressBookAPI(TestCase):
    """
    Test address book API requests.
    """
    
    def setUp(self):
        self.client = APIClient()
        
    def test_retrieve_contacts(self):
        """
        Test retrieving a list of contacts.
        """
        create_contact('Amrizal Fajar')
        create_contact('Digireg Indonesia')
        
        res = self.client.get(ADDRESS_BOOK_URL)
        
        contacts = models.AddressBook.objects.all().order_by('-id')
        