from django import forms
from .models import PersonalInfo, ContactInfo, EmergencyContact

class PersonalInfoForm(forms.ModelForm):
    # Define an optional employee_name field for manual entry
    employee_name = forms.CharField(required=False)

    class Meta:
        model = PersonalInfo
        fields = ['employee_name', 'date_of_birth', 'address']  # Add other fields as needed

    def clean_employee_name(self):
        employee_name = self.cleaned_data.get('employee_name')
        # You can perform additional validation or processing here
        return employee_name

class ContactInfoForm(forms.ModelForm):
    # Define an optional employee_name field for manual entry
    # employee_name = forms.CharField(required=False)
    class Meta:
        model = ContactInfo
        fields = ['email', 'phone_number']  # Add other fields as needed

    def clean_employee_name(self):
        employee_name = self.cleaned_data.get('employee_name')
        # You can perform additional validation or processing here
        return employee_name

class EmergencyContactForm(forms.ModelForm):
    # Define an optional employee_name field for manual entry
    # employee_name = forms.CharField(required=False)
    class Meta:
        model = EmergencyContact
        fields = ['guardian_name', 'relationship', 'phone_number']  # Add other fields as needed

    def clean_employee_name(self):
        employee_name = self.cleaned_data.get('employee_name')
        # You can perform additional validation or processing here
        return employee_name

# class CustomOTPVerificationForm(forms.Form):
#     otp_token = forms.CharField(label='Enter OTP', max_length=6)
