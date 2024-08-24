from django.shortcuts import redirect


def user_not_authenticated(functions=None, redirect_urls='/'):
    """
    """
    def decorator(view_func):
        def _wrapped_view(request,*args,**kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_urls)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    if functions:
        return decorator(functions)
    
    return decorator

def user_not_superuser(functions=None, redirect_urls='/'):
    """
    """
    def decorator(view_func):
        def _wrapped_view(request,*args,**kwargs):
            if not request.user.is_superuser:
                return redirect(redirect_urls)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    if functions:
        return decorator(functions)
    
    return decorator
