#coding=utf-8
from django.urls import path
from . import views
urlpatterns = [
    path('', views.helloworld, name='hello'),
    path('testData',views.testData,name='testData')
    path('KgBaseInfoFillin/',views.KgBaseInfoFillin,name='KgBaseInfoFillin'),#填写志愿信息
    path('KgBaseInfoFillin/questions/',views.InfoIntoQuestions,name="InfoIntoQuestions"),#返回志愿问题
]