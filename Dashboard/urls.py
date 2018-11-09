from django.contrib import admin
from django.urls import path, include
from Dashboard import views
from Dashboard.views import *

urlpatterns = [
    path('', views.index, name='employeeDashboard'),
    path('logout', views.employee_logout, name='employee_logout'),
    path('home', views.home_view, name='home_view'),
    path('availability', views.availability_view, name='availability_view'),
    path('timeoff', views.timeoff_view, name='timeoff_view'),
    path('schedule', views.shifts_view, name='shifts_view'),
]
