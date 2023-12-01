from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Slider, Service, Client, Faq, Gallery
from django.views.generic import ListView, DetailView, TemplateView


class HomeView(ListView):
    template_name = 'market/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['experts'] = Client.objects.all()
        return context


class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = "market/services.html"


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = "market/service_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class ClientListView(ListView):
    template_name = 'market/team.html'
    queryset = Client.objects.all()
    paginate_by = 8


class ClientDetailView(DetailView):
    template_name = 'market/team-details.html'
    queryset = Client.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Clients"] = Client.objects.all()
        return context


class FaqListView(ListView):
    template_name = 'market/faqs.html'
    queryset = Faq.objects.all()


class GalleryListView(ListView):
    template_name = 'market/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9


class ContactView(TemplateView):
    template_name = "market/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "Contact"

        if name and message and email and phone:
            send_mail(
                subject+"-"+phone,
                message,
                email,
                ['sandradhaneesh0789@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, " Email hasbeen sent successfully...")

        return redirect('contact')
