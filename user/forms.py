from django import forms
from .models import OlxUserProfile


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"readonly": "readonly"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"readonly": "readonly"}))

    class Meta:
        model = OlxUserProfile
        fields = ['firstname', 'lastname', 'phone', 'country', 'state', 'district', 'email', 'password', 'confirm_password']