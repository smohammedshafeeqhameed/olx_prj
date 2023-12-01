from django.urls import path
from .views import register, registration_view

urlpatterns = [
    path('', register, name='register'),
    path('register/', registration_view, name='registration'),  # Example registration URL pattern
]
