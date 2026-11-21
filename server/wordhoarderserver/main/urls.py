from django.urls import path
from .views import auth_test

urls = [
    path('auth_test/', auth_test),
]