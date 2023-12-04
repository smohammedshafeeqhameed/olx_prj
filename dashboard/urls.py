from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from .decorators import admin_only

app_name = "dashboard"

urlpatterns = [
    path("", admin_only(views.UserListView.as_view()), name="dashboard")
]