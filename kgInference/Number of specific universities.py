from django.http import HttpResponse
from django.shortcuts import render
from ormDesign.models import *
from django.db.models import Max,Min,Count,Sum,Avg
# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World! by kgInference group')

def get_data_985():

    Colleges_985=Colleges.objects.filter(project985=True)

    content=Colleges_985.objects.values('collegeID').annotate(Count=Count('collegeID')).order_by()
    data_lable=[]
    for i in range(35):
        data_lable.append(content[i])
    dict={'name': '985',
            'type': 'bar',
            'data':data_lable}

    return dict


def get_data_211():

    Colleges_211=Colleges.objects.filter(project211=True)

    content=Colleges_211.objects.values('collegeID').annotate(Count=Count('collegeID')).order_by()
    data_lable=[]
    for i in range(35):
        data_lable.append(content[i])
    dict={'name': '211',
            'type': 'bar',
            'data':data_lable}

    return dict


def get_data_double():

    Colleges_double=Colleges.objects.filter(top=True)

    content=Colleges_double.objects.values('collegeID').annotate(Count=Count('collegeID')).order_by()
    data_lable=[]
    for i in range(35):
        data_lable.append(content[i])
    dict={'name': '双一流',
            'type': 'bar',
            'data':data_lable}

    return dict
def get_data():
    series=[]
    series.append(get_data_985())
    series.append(get_data_211())
    series.append(get_data_double())
    return series


