"""signup URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('account', views.account, name='account'),
]
