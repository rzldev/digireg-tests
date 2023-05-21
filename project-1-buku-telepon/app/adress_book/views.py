"""
Views for the address book APIs.
"""

from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Contact, AddressBook

from adress_book.serializers import ContactSerializer, AddressBookSerializer

class AddressBookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Manage address book in the database.
    """
    serializer_class = AddressBookSerializer
    queryset = AddressBook.objects.all()
    
class ContactViewSet(mixins.ListModelMixin, 
                     mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin, 
                     viewsets.GenericViewSet):
    """
    Manage contact in the database.
    """
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    