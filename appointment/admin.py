from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'Client', 'date', 'time']
    date_hierarchy = ('date')
    list_filter = ['date', 'Client', ]
    list_per_page = 20
    search_fields = ['Client', 'name', ]
