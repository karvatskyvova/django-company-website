# crm/urls.py

from django.urls import path
from .views import clients_view

urlpatterns = [
    path('', clients_view, name='clients'),
]
