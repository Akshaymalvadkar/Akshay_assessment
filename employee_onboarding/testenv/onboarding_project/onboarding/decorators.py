from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Administrators').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper

def manager_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Managers').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper

def employee_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Employees').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper
