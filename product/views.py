from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.list import ListView
from product.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired

