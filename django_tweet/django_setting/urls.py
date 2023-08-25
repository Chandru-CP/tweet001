from django.urls import path
from . import views

urlpatterns = [
    path('setting/', views.settings_view, name='settings'),
]
