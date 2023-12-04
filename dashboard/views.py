from django.shortcuts import render
from django.views.generic import ListView

from user.models import OlxUser
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserListView(ListView, LoginRequiredMixin):
    template_name = "dashboard/dashboard.html"
    model = OlxUser
    context_object_name = 'user_list'