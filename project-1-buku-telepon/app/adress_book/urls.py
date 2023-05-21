"""
URL mappings for address book APIs.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from adress_book import views 

app_name = 'address_book'

router = DefaultRouter()
router.register('address-book', views.AddressBookViewSet),
router.register('contact', views.ContactViewSet),

urlpatterns = [
    path('', include(router.urls)),
]