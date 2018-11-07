from django.contrib import admin
from django.urls import path, include
from Dashboard import views
from Dashboard.views import *

urlpatterns = [
    path('', views.index, name='employeeDashboard'),
    path('logout', views.employee_logout, name='employee_logout')
]