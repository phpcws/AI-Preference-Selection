import pandas as pd
import json
import string
import os.path
import math
def getrecommendation(province,category,bl,rank,gradelist,ability=False):
    m=bl['Major'].tolist()
    majors=[]
    for major in m:
        if major not in majors:
            majors.append(major)
    ss=[]
    for major in majors:
        recommendation,risk=evaluate(province,category,bl,major,rank,gradelist)
        ss.append([recommendation,risk,major])
        
    ss.sort(reverse=True) 
    return ss[:5]



def evaluate(province,category,bl,major,rank,gradelist,ability=False):
    rank9=getrank(province,category,bl,major,2019)
    rank8=getrank(province,category,bl,major,2018)
    rank7=getrank(province,category,bl,major,2017)
    
    w9=0.4 if rank9!=-1 else 0
    w8=0.3 if rank8!=-1 else 0
    w7=0.3 if rank7!=-1 else 0
    
    r9=0.5*(rank9-rank) if (rank9-rank)>0 else rank-rank9
    r8=0.5*(rank8-rank) if (rank8-rank)>0 else rank-rank8
    r7=0.5*(rank7-rank) if (rank7-rank)>0 else rank-rank7
    
    d9=rank-rank9
    d8=rank-rank8
    d7=rank-rank7
    
    
    if((w9+w8+w7)!=1 and (w9+w8+w7)!=0):
        r=1/(w9+w8+w7)
        w9=r*w9
        w8=r*w8
        w7=r*w7

    x=(r9*w9+r8*w8+r7*w7)*0.04
    recommendation=2/(1+math.exp( x ))
    
    y=(d9*w9+d8*w8+d7*w7)*0.04
    risk=1/(1+math.exp(-y))
    return recommendation,risk

    
def getrank(province,category,bl,subject,year):
    bl=bl[bl['Year']==year]
    if(category=='不分文理'):
        category='all'
    score=bl[bl['Major']==subject]['score'].tolist()
    if score:
        score=score[0]
    else:
        return -1

    file='json_csv(09150017)/'+str(year)+province+category+'.csv'
    rank=pd.read_csv(file,encoding='utf-8') 
    rank=rank[rank["分数"]==score]["累计人数"].tolist()
    if rank:
        rank=rank[0]
    else:
        return -1
    return rank
    


province='江苏'
category='理科'
college='同济大学'
#grade=400
rank=1500
subjects=[]
borderline=pd.read_csv('高校录取分数线整合（省份名字统一）.csv',encoding='utf-8')
bl= borderline[borderline['Province']==province]
bl= bl[bl['category']==category]
bl= bl[bl['College']==college]

rrc=getrecommendation(province, category, bl, rank)
rrc=pd.DataFrame(rrc, columns=['推荐度', '风险值', '专业'])
print(rrc)
f=province+category+college+str(rank)+".csv"
rrc.to_csv(f, sep=',', header=True, index=False,encoding='utf-8-sig')
#with open()

