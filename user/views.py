from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user import forms
from user.models import OlxUser
from django.contrib.auth.models import Group

import secrets

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.views.generic import TemplateView, View
from django.contrib.auth.views import PasswordResetView



def generate_random_six_digit_number():
    return secrets.randbelow(1000000)

def send_email(email, password):
        subject = 'Subject'
        html_message = render_to_string('user/register_email.html', {'email': email, 'password': password})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

# Create your views here.
class RegistrationView(CreateView):

    form_class = forms.RegistrationForm
    success_url = reverse_lazy("user:login")
    template_name = "user/register.html"

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
         print(form.cleaned_data)
         return super().form_invalid(form)

    def form_valid(self, form):
        print(form.cleaned_data)
        
        user_profile = form.save(commit=False)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = OlxUser.objects.create_user(email=email, password=password, username=email)

        

        user_profile.user = user
        user_profile.save()

        customer, created = Group.objects.get_or_create(name="Customer")
        user.groups.add(customer)


        send_email(email, password)


        response = super().form_valid(form)

        response.set_cookie('registration_success', 'true', max_age=60)

        return response

class PassView(PasswordResetView):
    """View for reseting user password"""

    success_url = reverse_lazy("user:password-success")


class PassSuccess(TemplateView):
    """View for displaying template after successful password reset"""

    template_name = "user/password_success.html"

    
class UserApproveView(View):
     

     def get(self, request):
        approve = int(request.GET.get('approve'))
        id = request.GET.get('id')
        user = OlxUser.objects.get(id=id)
        user.is_approved = approve
        user.save()

        return redirect(reverse_lazy('dashboard:dashboard'))
