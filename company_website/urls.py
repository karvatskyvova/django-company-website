# company_website/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navigation/', include('navigation.urls')),
    path('services/', include('services.urls')),
    path('crm/', include('crm.urls')),
]
