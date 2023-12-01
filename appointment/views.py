from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from market.models import Client
from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'Clients': Client.objects.all()
        }
        return render(request, "appointment/register.html", context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Client_id = request.POST.get('Client')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')
        if Client_id:
            Client = get_object_or_404(Client, id=Client_id)

        if(name and phone and email and Client and date and time):
            Appointment.objects.create(
                name=name, phone=phone, email=email, Client=Client, date=date, time=time, note=note)
            messages.success(request,'Appointment done successfully')
        return redirect('appointment')
