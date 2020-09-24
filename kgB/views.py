import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import get_nodelist, get_relationshiplist, get_provincedict
# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World!')

def kgB_index(request):
    province = get_provincedict()
    return render(request, 'kgB_index.html', {'province': province})

def kg_province(request):
    province = request.GET.get("select_province", '')
    node = get_nodelist(str(province))
    edge = get_relationshiplist(node)
    request.encoding = 'utf-8'
    return render(request, 'kg_province.html', {'node': json.dumps(node), 'edge': json.dumps(edge)})
