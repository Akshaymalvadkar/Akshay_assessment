from django.urls import path, include
from . import views

urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
    path('', views.custom_login, name='login'),
    path('emp_register/', views.register, name='register'),
    path('logout/', views.custom_login, name='logout'),
    path('onboarding/admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('onboarding/manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('onboarding/employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
]
