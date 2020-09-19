import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import get_nodelist, get_relationshiplist
# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World!')

def kgBIndex(request):
    return render(request, 'kgBIndex.html')

def jiangsu04(request):
    node = get_nodelist('江苏')
    edge = get_relationshiplist(node)
    return render(request, 'jiangsu04.html', {'node': json.dumps(node), 'edge': json.dumps(edge)})