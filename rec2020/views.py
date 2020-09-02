#coding=utf-8
import random

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #测试数据，实际使用时需要从数据库读取相关数据，以构建下拉菜单
    province = {"1": "北京", "2": "天津", "3":"江苏"}
    category = {"1": "理科", "2": "文科", "3":"不分文理"}
    return render(request, 'index.html', {'province': province, 'category':category})

def recResuts(request):
    # 测试数据，需要从数据库读取相关数据，以返回推荐结果
    request.encoding = 'utf-8'
    province = request.GET.get("select_province", '')
    category = request.GET.get("select_category", '')
    university_id = str(random.randint(1, 100))
    message = "测试数据:"+province+category+"排名第"+university_id+"的好大学！"
    return HttpResponse(message)

