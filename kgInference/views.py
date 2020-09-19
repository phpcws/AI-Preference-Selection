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
def KgBaseInfoFillin(request):
    return render(request, 'KgBaseInfoFillin.html')
    
def InfoIntoQuestions(request):  #将用户输入信息转化成更具体的问题，经用户选择具体问题后生成图标。by:陈震寰&张立创
    province = request.POST.get('province')
    score = request.POST.get('score')
    score = int(score)
    subject = request.POST.get('subject')
    targetprovince = request.POST.get('Tprovince')
    targetmajor = request.POST.get('Tmajor')
    questions = []

    if(targetprovince == "" and targetmajor == ""):
        questionhead = province + str(score) + "分"
        question11 = questionhead + "冲一冲能上什么学校？"
        question12 = questionhead + "稳一稳能上什么学校？"
        questions.append(question11)
        questions.append(question12)
        #schooltype = "普通一本"
        if(province == "江苏"):
            if(score >= 390):
                question13 = questionhead + "能上什么985学校?"
                questions.append(question13)
            if (score >= 370 and score < 390):
                question13 = questionhead + "能上什么985学校?"
                question14 = questionhead + "能上什么211学校?"
                questions.append(question13)
                questions.append(question14)
            if (score < 370 and score >= 360):
                question13 = questionhead + "能上什么211学校?"
                question14 = questionhead + "能上什么一本学校？"
                questions.append(question13)
                questions.append(question14)
            if(score < 360):
                question13 = questionhead + "能上什么一本学校？"
                questions.append(question13)

        elif(province == "上海"):
            if(score >= 560):
                question13 = questionhead + "能上什么985学校?"
                questions.append(question13)
            if (score >= 510 and score < 560):
                question13 = questionhead + "能上什么985学校?"
                question14 = questionhead + "能上什么211学校?"
                questions.append(question13)
                questions.append(question14)
            if (score < 510 and score >= 450):
                question13 = questionhead + "能上什么211学校?"
                question14 = questionhead + "能上什么一本学校？"
                questions.append(question13)
                questions.append(question14)
            if(score < 450):
                question13 = questionhead + "能上什么一本学校？"
                questions.append(question13)

        else:
            if(score >= 660):
                question13 = questionhead + "能上什么985学校?"
                questions.append(question13)
            if (score >= 620 and score < 660):
                question13 = questionhead + "能上什么985学校?"
                question14 = questionhead + "能上什么211学校?"
                questions.append(question13)
                questions.append(question14)
            if (score < 620 and score >= 590):
                question13 = questionhead + "能上什么211学校?"
                question14 = questionhead + "能上什么一本学校?"
                questions.append(question13)
                questions.append(question14)
            if(score < 590):
                question13 = questionhead + "能上什么一本学校？"
                questions.append(question13)


    if(targetprovince != "" and targetmajor == ""):
        questionhead = province + str(score) + "分"
        question21 = questionhead + "冲一冲能上" + targetprovince + "的什么学校？"
        question22 = questionhead + "稳一稳能上" + targetprovince + "的什么学校？"
        question23 = targetprovince + "大学分数线排名"
        questions.append(question21)
        questions.append(question22)
        questions.append(question23)
        schooltype = "普通一本"

        if(province == "江苏"):
            if(score >= 390):
                question24 = questionhead + "能上" + targetprovince + "的什么985学校?"
                questions.append(question24)
            if (score >= 370 and score < 390):
                question24 = questionhead + "能上" + targetprovince + "的什么985学校?"
                question25 = questionhead + "能上" + targetprovince + "的什么211学校?"
                questions.append(question24)
                questions.append(question25)
            if (score < 370 and score >= 360):
                question24 = questionhead + "能上" + targetprovince + "的什么211学校?"
                question25 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question24)
                questions.append(question25)
            if(score < 360):
                question24 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question24)

        elif(province == "上海"):
            if(score >= 560):
                question24 = questionhead + "能上" + targetprovince + "的什么985学校?"
                questions.append(question24)
            if (score >= 510 and score < 560):
                question24 = questionhead + "能上" + targetprovince + "的什么985学校?"
                question25 = questionhead + "能上" + targetprovince + "的什么211学校?"
                questions.append(question24)
                questions.append(question25)
            if (score < 510 and score >= 450):
                question24 = questionhead + "能上" + targetprovince + "的什么211学校?"
                question25 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question24)
                questions.append(question25)
            if(score < 450):
                question24 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question24)

        else:
            if(score >= 660):
                question24 = questionhead + "能上" + targetprovince + "什么985学校?"
                questions.append(question24)
            if (score >= 620 and score < 660):
                question24 = questionhead + "能上" + targetprovince + "的什么985学校?"
                question25 = questionhead + "能上" + targetprovince + "的什么211学校?"
                questions.append(question24)
                questions.append(question25)
            if (score < 620 and score >= 590):
                question24 = questionhead + "能上" + targetprovince + "的什么211学校?"
                question25 = questionhead + "能上" + targetprovince + "的什么一本学校?"
                questions.append(question24)
                questions.append(question25)
            if(score < 590):
                question24 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question24)

    if(targetprovince == "" and targetmajor != ""):
        question31 = targetmajor + "专业" + "全国大学排名"
        question32 = province + str(score) + "分" + "哪些学校的" + targetmajor + "专业" + "性价比比较高？"
        question33 = province + str(score) + "分" + "能上哪些学校的" + targetmajor + "专业？"
        questions.append(question31)
        questions.append(question32)
        questions.append(question33)

    if(targetprovince != "" and targetmajor != ""):
        question41 = province + str(score) + "在" + targetprovince + "哪些学校的" + targetmajor + "专业性价比比较高？"
        question42 = targetprovince + targetmajor + "专业大学排名"
        questions.append(question41)
        questions.append(question42)

        questionhead = province + str(score) + "分在" + targetprovince + "能上什么"
        if(province == "江苏"):
            if(score >= 390):
                question43 = questionhead + "985学校?"
                questions.append(question43)
            if (score >= 370 and score < 390):
                question43 = questionhead + "985学校?"
                question44 = questionhead + "211学校?"
                questions.append(question43)
                questions.append(question44)
            if (score < 370 and score >= 360):
                question43 = questionhead + "211学校?"
                question44 = questionhead + "一本学校？"
                questions.append(question43)
                questions.append(question44)
            if(score < 360):
                question43 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question43)

        elif(province == "上海"):
            if(score >= 560):
                question43 = questionhead + "985学校?"
                questions.append(question43)
            if (score >= 510 and score < 560):
                question43 = questionhead + "985学校?"
                question44 = questionhead + "211学校?"
                questions.append(question43)
                questions.append(question44)
            if (score < 510 and score >= 450):
                question43 = questionhead + "211学校?"
                question44 = questionhead + "一本学校？"
                questions.append(question43)
                questions.append(question44)
            if(score < 450):
                question43 = questionhead + "能上" + targetprovince + "的什么一本学校？"
                questions.append(question43)

        else:
            if(score >= 660):
                question43 = questionhead + "985学校?"
                questions.append(question43)
            if (score >= 620 and score < 660):
                question43 = questionhead + "985学校?"
                question44 = questionhead + "211学校?"
                questions.append(question43)
                questions.append(question44)
            if (score < 620 and score >= 590):
                question43 = questionhead + "211学校?"
                question44 = questionhead + "一本学校?"
                questions.append(question43)
                questions.append(question44)
            if(score < 590):
                question43 = questionhead + "一本学校？"
                questions.append(question43)
    return render(request,'KgInfoToQuestion.html',{'questions':questions})
