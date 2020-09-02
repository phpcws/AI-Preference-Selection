#coding=utf-8
from django.urls import path
from . import views
urlpatterns = [
    path('', views.helloworld, name='hello'),
    path('graph/', views.get_json_new, name='graph'),
]