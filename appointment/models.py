from django.db import models
from market.models import Client
from django.utils import timezone


class Appointment(models.Model):
    time_choices = (
        ('morning', "Morning"),
        ('evening', "Evening")
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    Client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=time_choices, max_length=10)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.Client.name}"
