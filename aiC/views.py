from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World! by aiC group')