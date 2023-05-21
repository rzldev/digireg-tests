"""
Database models.
"""
from django.db import models

class AddressBook(models.Model):
    """
    Address book class.
    """
    
    def __str__(self):
        return self.id

class Contact(models.Model):
    """
    Contact class.
    """
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    address_book = models.ForeignKey(AddressBook, on_delete=models.CASCADE, related_name='address_book')
    
    def __str__(self):
        return self.id
    