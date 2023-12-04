from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

app_name = "product"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="products")
]