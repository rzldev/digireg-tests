"""
Test Django models.
"""

from django.test import TestCase

from core import models

class TestModels(TestCase):
    """
    Model tests.
    """
    
    def test_create_contact(self):
        """
        Test creating a contact.
        """
        phone_number = '+6289123452833'
        contact = models.Contact.objects.create(
            name='Amrizal Fajar',
            telephone=phone_number,
        )
        
        self.assertEqual(str(contact), contact.name)
        self.assertEqual(contact.telephone, phone_number)
        
    def test_create_address_book(self):
        """
        Test creating an address book.
        """
        contact1 = models.Contact.objects.create(
            name='Amrizal Fajar',
            telephone='+6249123352987'
        )
        address_book = models.AddressBook.objects.create(
            contacts=contact1,
        )
        
        self.assertEqual(address_book.contacts.name, contact1.name)
        self.assertEqual(address_book.contacts.telephone, contact1.telephone)
        