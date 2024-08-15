from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def user_not_authenticated(function=None, redirect_url='/'):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the homepage if necessary by default.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator



def user_is_superuser(function):
    """
    Decorator to restrict access to superusers only.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            # User is a superuser, allow access to the view
            return function(request, *args, **kwargs)
        else:
            # User is not a superuser, forbid access
            return HttpResponseForbidden("You don't have permission to access this page.")

    return wrapper