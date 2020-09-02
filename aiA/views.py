from django.http import HttpResponse
from django.shortcuts import render
app_name = 'aiA'
# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World! by aiA group')