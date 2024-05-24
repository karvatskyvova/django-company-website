# crm/views.py

from django.shortcuts import render
from .models import Client

def clients_view(request):
    clients = Client.objects.all()
    return render(request, 'crm/clients.html', {'clients': clients})
