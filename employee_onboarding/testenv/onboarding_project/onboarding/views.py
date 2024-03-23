from .models import Employee
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .forms import PersonalInfoForm, ContactInfoForm, EmergencyContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .decorators import admin_required, manager_required, employee_required
# from two_factor.views import OTPRequiredMixin
# from .forms import CustomOTPVerificationForm

@login_required
def onboarding(request):
    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST)
        contact_info_form = ContactInfoForm(request.POST)
        emergency_contact_form = EmergencyContactForm(request.POST)
        if personal_info_form.is_valid() and contact_info_form.is_valid() and emergency_contact_form.is_valid():
            # Save forms
            personal_info = personal_info_form.save(commit=False)
            personal_info.employee = request.user.employee
            personal_info.save()

            contact_info = contact_info_form.save(commit=False)
            contact_info.employee = request.user.employee
            contact_info.save()

            emergency_contact = emergency_contact_form.save(commit=False)
            emergency_contact.employee = request.user.employee
            emergency_contact.save()

             # Display popup message
            messages.success(request, 'Welcome to the Board')

            # Redirect to respective dashboard based on user role
            # Handle form submission
            if 'manager' in request.POST.getlist('roles'):
                # Redirect to manager dashboard
                return redirect('manager_dashboard')
            elif 'administrator' in request.POST.getlist('roles'):
                # Redirect to administrator dashboard
                return redirect('admin_dashboard')
            else:
                # Redirect to employee dashboard or display error message
                return redirect('employee_dashboard')

    else:
        personal_info_form = PersonalInfoForm()
        contact_info_form = ContactInfoForm()
        emergency_contact_form = EmergencyContactForm()
    return render(request, 'onboarding.html', {'personal_info_form': personal_info_form, 'contact_info_form': contact_info_form, 'emergency_contact_form': emergency_contact_form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to a success page
                return redirect('onboarding') 
            else:
                # Handle invalid login
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# def login_with_otp(request):
    # if request.method == 'POST':
    #     form = OTPAuthenticationForm(request.POST)
    #     if form.is_valid():
    #         login(request, form.get_user())
    #         return redirect('dashboard')
    # else:
    #     form = OTPAuthenticationForm()
    # return render(request, 'login_with_otp.html', {'form': form})

# class CustomOTPVerificationView(OTPRequiredMixin):
#     form_class = CustomOTPVerificationForm
#     template_name = 'otp_verification.html'
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'emp_register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            # return redirect('onboarding')  # Redirect to onboarding page after successful registration
            if user is not None:
                auth_login(request, user)
                return redirect('login')  # Redirect to onboarding page after successful registration
            else:
                print("User authentication failed.")
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'emp_register.html', {'form': form})


def initialize_roles():
    # Create groups
    admin_group, _ = Group.objects.get_or_create(name='Administrators')
    manager_group, _ = Group.objects.get_or_create(name='Managers')
    employee_group, _ = Group.objects.get_or_create(name='Employees')

    admin_user = User.objects.get(username='admin')
    admin_user.groups.add(admin_group)

    manager_user = User.objects.get(username='manager')
    manager_user.groups.add(manager_group)

    employee_user = User.objects.get(username='employee')
    employee_user.groups.add(employee_group)
    return HttpResponse("User roles initialized successfully.")

@admin_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@manager_required
def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')

@employee_required
def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')
