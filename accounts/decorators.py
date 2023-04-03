from django.shortcuts import render, redirect


def authenticated_user(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)

        return redirect("login")

    return wrap


def unauthenticated_user(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrap


def required_permissions(perm_list=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if perm_list:
                for perm in request.user.permissions.all():
                    if perm.name in perm_list:
                        return view_func(request, *args, **kwargs)
                return render(request, "error_404.html")
            return render(request, "error_404.html")

        return wrap

    return decorator
