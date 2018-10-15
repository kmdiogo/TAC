from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_student', views.create_student, name='create_student'),
    path('school_id_taken', views.school_id_taken, name='school_id_taken'),
]

# www.mysite.com
