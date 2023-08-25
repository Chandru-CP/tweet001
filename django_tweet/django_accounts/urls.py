from django.urls import path
import views
from tweet.django_tweet.django_homepage import views as home_views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('homepage/',home_views.homepage_view, name='homepage'),
]
