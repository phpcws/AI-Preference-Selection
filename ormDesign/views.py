from django.http import HttpResponse
from ormDesign import models
from django.shortcuts import render
app_name = 'ormDesign'

import os
import pandas as pd
import numpy as np
filename=os.getcwd()


def getCategory(request):
    c1=models.Category(categoryID=1,categoryname="文科")
    c1.save()
    c1 = models.Category(categoryID=2, categoryname="理科")
    c1.save()
    c1 = models.Category(categoryID=3, categoryname="综合")
    c1.save()
    return HttpResponse("Category in!")


def getProvinces(request):
    data=pd.read_csv('./extFiles/省份.csv',encoding="gbk")
    num = data.shape[0]
    for i in range(num):
        id = data.values[i][0]
        name = data.values[i][1]
        c1=models.Provinces(provinceID=id,
                            provinceName=name,
        )
        c1.save()
    return HttpResponse('Provinces in!')


def getFirstLevel(request):
    data=pd.read_csv('./extFiles/一级学科.csv',encoding="gbk")
    num=data.shape[0]
    for i in range(num):
        if data.values[i][0]<15:
            FstName =data.values[i][1]
            FstID=data.values[i][0]
        else:
            id0=data.values[i][0]
            name0=data.values[i][1]
            c1 = models.Firstlevel(
                firstlevelName=name0,
                subjectName=FstName,
                subjectID=FstID,
                firstlevelID=id0
            )
            c1.save()
    return HttpResponse('First Level in!')

def getColleges(request):
    df = pd.read_csv('./extFiles/college.csv', encoding="gbk")
    num = df.shape[0]
    for x in range(num):
        c2 = models.Colleges(collegeID=df.at[x, 'collegeID'],
                             collegeName=df.at[x, 'collegeName'],
                             provinceID=models.Provinces.objects.get(provinceName=df.at[x,'province']),
                             project985=df.at[x, '985'],
                             project211=df.at[x, '211'],
                             top=df.at[x, 'top'])
        c2.save()
    return HttpResponse("College in")


def getMajors(request):
    df=pd.read_csv('./extFiles/高校录取分数线整合（省份名字统一）.csv')
    num=df.shape[0]
    for i in range(num):
        if df.at[i,'category']=='不分文理':
            df.at[i,'category']='综合'
        if df.at[i, 'College']=='华东理科大学':
            df.at[i, 'College']='华东理工大学'
        if df.at[i, 'College'] == '北京理科大学':
            df.at[i, 'College'] = '北京理工大学'
        if df.at[i, 'College'] == '\ufeff北京航空航天大学':
            df.at[i, 'College'] = '北京航空航天大学'
        c1=models.Majors(majorName=df.at[i,'Major'],
                    year=df.at[i,'Year'],
                    id=i,
                    categoryID=models.Category.objects.get(categoryname=df.at[i,'category']),
                    minScore=df.at[i,'score'],
                    collegeID=models.Colleges.objects.get(collegeName=df.at[i,'College']),
                    provinceID=models.Provinces.objects.get(provinceName =  df.at[i,'Province']))
        c1.save()
    return HttpResponse("Majors in!")


def getRankings(request):
    filename=os.getcwd()
    dirs = os.listdir(filename+'\\extFiles'+'\\json\\')
    for i in range(0, 110):  # 文件个数

        df = pd.read_csv(
            filename+'\\extFiles'+ '\\json\\' + dirs[i],encoding='gbk')  # 返回一个DataFrame的对象，这个是pandas的一个数据结构

        df.columns = ["Col1", "Col2", "Col3","Col4","Col5"]

        X = df[["Col1", "Col2", "Col3","Col4","Col5"]]  # 抽取前七列作为训练数据的各属性值

        y= np.array(X)  # 存到数组中
        op=len(y)
        for p in range(0,op):


           c1=models.Rankings(

               provinceID=models.Provinces.objects.get(provinceID=y[p][2]),
               score=y[p][0],
               rank=y[p][1],
               categoryID=models.Category.objects.get(categoryname=y[p][4]),
               year=y[p][3],
        )
           c1.save()
    return HttpResponse('Rankings in')