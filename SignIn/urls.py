from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_student', views.create_student, name='create_student')
]

# www.mysite.com
