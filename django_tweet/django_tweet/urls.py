from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_accounts.urls')),  # Include your signup app URLs
    path('homepage/', include('django_homepage.urls')),  # Include your homepage app URLs
    path('profile/', include('django_profile.urls')),  # Include your profile app URLs
    path('settings/', include('django_setting.urls')),  # Include your settings app URLs
]
