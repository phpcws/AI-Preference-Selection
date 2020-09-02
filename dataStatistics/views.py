#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
app_name = 'dataStatistics'
# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World! by dataStatistics group')

# 折线图对应的的模板
def showlinediagram(request):
    return render(request, 'linediagram.html')
