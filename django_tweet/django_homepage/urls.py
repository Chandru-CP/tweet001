from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage_view, name='homepage'),
]
