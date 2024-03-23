from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    # Define your fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        app_label = 'onboarding'

class PersonalInfo(models.Model):
    # employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    # Add personal information fields
    date_of_birth = models.DateField()
    address = models.TextField()

class ContactInfo(models.Model):
    # employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    # Add contact information fields
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

class EmergencyContact(models.Model):
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Add emergency contact fields
    guardian_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
