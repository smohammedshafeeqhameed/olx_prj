from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.core.mail import send_mail

from .utils import generate_random_password  # Import the function you created

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            generated_password = generate_random_password()  # Generate the random password
            user.set_password(generated_password)  # Set the generated password for the user
            user.save()
            #
            # # Send email with the generated password to the user
            # subject = 'Registration Confirmation'
            # message = f'Hello {user.name}, your password is: {generated_password}. Please use this password to log in.'
            # from_email = 'smohammed'  # Replace with your email address
            # send_mail(subject, message, from_email, [user.email])

            messages.success(request, 'Registration successful. Please check your email for confirmation.')
            return render(request, 'olx_app/register.html', {'form': form})
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'olx_app/register.html', {'form': form})


# Django views.py
import random
import string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from olx_app.models import UserProfile

def registration_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = ''.join(random.choices(string.digits, k=6))  # Generate a 6-digit password
        # Check email uniqueness
        if User.objects.filter(email=email).exists():
            # Display an error message for duplicate email
            error_message = "Email already exists. Please use a different email."
            print(error_message)
            return render(request, 'olx_app/register.html', {'error_message': error_message})
        else:
            # Create a new user with the generated password
            user = User.objects.create_user(username=email, email=email, password=password)
            # Send confirmation email to the user
            # send_confirmation_email(email, password)  # Implement send_confirmation_email function
            # return redirect('register')  # Redirect to a success page or login page
            print("Success")

    return render(request, 'olx_app/register.html')

def send_confirmation_email(email, password):
    # Implement the logic to send the confirmation email with the generated password
    # Use Django's send_mail function to send the email
    # Ensure proper formatting of the email and include the generated password
    # For example:
    send_mail(
        'Registration Confirmation',
        f'Hello, Thank you for registering! Your password is: {password}.',
        'your_email@example.com',
        [email],
        fail_silently=False,
    )

