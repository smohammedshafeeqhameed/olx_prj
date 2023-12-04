from django.shortcuts import redirect
from django.urls import reverse


def admin_only(view_func):
    """redirect customer when the try to access admin dashboard."""

    def wrapper_func(request, *args, **kwargs):
        group = None
        print(request.user)
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "Admin":
            return view_func(request, *args, **kwargs)
        if group == "Customer":
            return redirect(reverse("product:products"))
        if not group:
            return redirect(reverse("product:products"))

    return wrapper_func