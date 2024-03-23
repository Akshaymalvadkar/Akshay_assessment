from django.contrib import admin
from .models import Employee, PersonalInfo, ContactInfo, EmergencyContact

# Register your models here.

admin.site.register(Employee)
admin.site.register(PersonalInfo)
admin.site.register(ContactInfo)
admin.site.register(EmergencyContact)