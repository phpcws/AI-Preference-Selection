import pandas as pd





def subjectscore(major,gradelist):#province
    ability=getabl(major)
    
    sub2abl=getsub2abl()
    
    score=0
    advancesub=[]
    for key,values in gradelist.items():
        if(key=='数学' or key=='语文' or key=='外语'):
            if values>135:
                advancesub.append(key)
        else:
            if values>90:
                advancesub.append(key)
                
    for subject in advancesub:
        abls=sub2abl[subject]
        for abl in abls:
            if abl in ability:
                score+=1
        
    return score
    

#获得能加分的能力 
def getabl(major):
    maj2maj1=getmaj2maj1()
    maj12sg=getmaj12sg()
    sg2abl=getsg2abl()
    #加载字典
    
    ability=[]
    
    major1=maj2maj1[major]
    major1=major1.split(";")
    for temp1 in major1:
        sg=maj12sg[temp1]
        abilities=sg2abl[sg].split("，")
        for temp2 in abilities:
            if temp2 not in ability:
                ability.append(temp2)
    return ability


#科目对应能力
def getsub2abl():
    sub2abl={}
    with open('单科成绩-能力.txt','r+',encoding='utf-8') as f:
        for line in f:
            subject,abilities=line.split()
            ability=abilities.split('，')
            sub2abl[subject]=ability
    return sub2abl


#学群对应能力
def getsg2abl():
    sgcsv=pd.read_excel("学群能力对应关系.xlsx")
    sg=sgcsv["学群"]
    ability=sgcsv["需要能力"]
    sg2abl=dict(zip(sg,ability))
    return sg2abl
            
#一级学科对应学群
def getmaj12sg():
    maj12sg={}
    with open('一级学科-学群.txt','r+',encoding='utf-8') as f:
        for line in f:
            if(len(line.split())==2):
                major1,sg=line.split()
                id,major1=major1.split(",")
                maj12sg[major1]=sg
    return maj12sg
    

#具体学科对应一级学科
def getmaj2maj1():
    majorcsv=pd.read_csv('result.csv')
    major1=majorcsv['major2 (disambiguated)']
    major=majorcsv['major (origin)']  
    maj2maj1=dict(zip(major,major1))  
    return maj2maj1


major="纺织工程（普通类）"       
gradelist={"数学":140,"语文":130,"外语":120,"物理":90,"化学":100,"生物":90,"历史":70,"政治":80,"地理":80,"技术":80}
      

score=subjectscore(major,gradelist)    
print(score)
