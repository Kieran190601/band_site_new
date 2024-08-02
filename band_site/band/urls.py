# band/urls.py
from django.urls import path
from .views import landing_page, members, events, register

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('members/', members, name='members'),
    path('events/', events, name='events'),
    path('register/', register, name='register'),
]
