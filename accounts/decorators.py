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
