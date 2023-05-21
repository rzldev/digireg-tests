"""
Serializer for address book APIs.
"""

from rest_framework import serializers
from core.models import Contact, AddressBook

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for contact.
    """
    
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['id', 'address_book']
        
    def _get_or_create_address_book(self):
        """
        Handler getting or creating address book needed.
        """
        instance, _ = AddressBook.objects.get_or_create({'id': 1})
        return instance
        
    def create(self, validated_data):
        """
        Create contact.
        """
        address_book = self._get_or_create_address_book()
        validated_data['address_book'] = address_book
        return Contact.objects.create(**validated_data)
    
class AddressBookSerializer(serializers.ModelSerializer):
    """
    Serializer for address book.
    """
    contacts = ContactSerializer(many=False, required=False)

    class Meta:
        model = AddressBook
        fields = ['id', 'contacts']
        read_only_fields = ['id']
        
    def to_representation(self, instance):
        """
        Handles the response data.
        """
        ret = super().to_representation(instance)
        ret['contacts'] = Contact.objects.filter(address_book=instance).values()
        return ret       
    