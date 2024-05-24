# navigation/urls.py

from django.urls import path
from .views import navigation_view

urlpatterns = [
    path('menu/', navigation_view, name='menu'),
]
