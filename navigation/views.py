# navigation/views.py

from django.shortcuts import render
from .models import MenuItem

def navigation_view(request):
    menu_items = MenuItem.objects.all().order_by('order')
    return render(request, 'navigation/menu.html', {'menu_items': menu_items})
