from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='p4a_home'),
    path('portfolio/', views.portfolio, name='p4a_portfolio'),
    path('contacts/', views.contacts, name='p4a_contacts'),
]