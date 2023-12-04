"""Url conf for account related functionality"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "user"

urlpatterns = [
    path("register/",views.RegistrationView.as_view(template_name="user/register.html"),name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="user/login.html"),name="login",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("change-password/",views.PassView.as_view(template_name="user/password_change_form.html"),name="password-reset",),
    path("password-success/",views.PassSuccess.as_view(template_name="user/password_success.html"),name="password-success",),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path("approve/", views.UserApproveView.as_view(), name="approve")
]
