from django import forms
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'mobile_number', 'address', 'country', 'state', 'district', 'password']
