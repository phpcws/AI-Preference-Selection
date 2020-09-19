from django.http import HttpResponse
from django.shortcuts import render
from ormDesign.models import *

# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World! by kgInference group')

#Get certain major scores in different univ. and rank them

def getMajorScoresRanking(pID,cID,y,mName):
    #参数为省份ID（整数1-34），科类ID（整数1-3），年份（整数）和专业名称
    majorList=Majors.objects.filter(provinceID=pID,
                                    categoryID=cID,
                                    year=y,
                                    majorName=mName)
    scoresDict={}
    for major in majorList:
        scoresDict[major.collegeID.collegeName]=major.minScore
    #return scoresDict
    scoresOrder=dict(sorted(scoresDict.items(), key = lambda kv:kv[1],reverse=True))
    return scoresOrder

def testData(request):
    scoresRanking=getMajorScoresRanking(16,1,2018,"all")
    return render(request,"testData.html",{"scoresRanking":scoresRanking})