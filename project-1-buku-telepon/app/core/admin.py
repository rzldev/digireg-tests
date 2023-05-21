from django.contrib import admin

from core import models

# Register your models here.

admin.site.register(models.Contact)
admin.site.register(models.AddressBook)