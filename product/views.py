from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from product.models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin,ListView, FormView):
    model = Product
    paginate_by = 100
    object_list = Product.objects.all()
    form_class = ProductForm
    success_url = reverse_lazy('product:products')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.added_by = self.request.user
        product.save()
        return super(ProductListView, self).form_valid(form)
    
    def form_invalid(self,form):
        form = super(ProductListView, self).form_invalid(form)
        print(form)
        return form

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


