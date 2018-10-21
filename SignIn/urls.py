from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

# Router generates URL's for REST views
router = routers.DefaultRouter()
router.register('students', views.StudentView)
#router.register('sessions', views.OpenSessionsView)

urlpatterns = [
    path('', views.index, name='index'),
    path('tac-api/sessions/', views.CreateOpenSessionView.as_view()),
    path('tac-api/sessions/<pk>/', views.OpenSessionsView.as_view()),
    url(r'^tac-api/', include(router.urls)),

]

# www.mysite.com
