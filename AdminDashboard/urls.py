from django.contrib import admin
from django.urls import path, include
from AdminDashboard import views

urlpatterns = [
    path('', views.index, name='adminDashboard'),
]