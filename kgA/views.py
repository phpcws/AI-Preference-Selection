import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World! by kgA group')
def get_json_new(request):
    node = [{'data': {'id': '2', 'name':'kg1', 'label': '中国科学院计算技术研究所'}},\
            {'data': {'id': '5', 'name':'kg2', 'label': '中国科学院计算技术研究所'}},\
            {'data':{'id':'1001','label':'school','title':'中国科学院计算技术研究所'}}]
    edge = [{'data': {'source': '2', 'target': '1001', 'relationship': 'belong_to'}},\
            {'data': {'source': '5', 'target': '1001', 'relationship': 'belong_to'}}]
    return render(request,'kgA_index.html',{'node':json.dumps(node),'edge':json.dumps(edge)})