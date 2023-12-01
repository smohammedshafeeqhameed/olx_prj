from .models import Client, Service


def footer_content(request):
    services = Service.objects.all()
    Clients = Client.objects.all()
    context = {
        'services': services,
        'Clients': Clients
    }
    return context
