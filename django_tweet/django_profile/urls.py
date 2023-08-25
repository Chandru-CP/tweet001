from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
