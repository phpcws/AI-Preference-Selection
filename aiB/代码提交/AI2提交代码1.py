# -*- coding: utf-8 -*-


import csv
import os
import matplotlib.pyplot as plt
import re
import random
import numpy as np
import sqlite3 as db

######part1 从数据库中读取数据


def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory=db.Row     # 可访问列信息
    cursor.execute(exectCmd)    #该例程执行一个 SQL 语句
    rows=cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows

def readfromAppaFrame(ARPAFrame):
    subARPA=ARPAFrame.split(',')
    return subARPA

def get_dataset(path='./db.sqlite3'):
    dataset = []
    for provinceID in [i + 1 for i in range(34)]:
        for year in [i + 2017 for i in range(3)]:
            for categoryID in range(1,4):
                sql = 'select score,rank from Rankings where provinceID_id=%s and year=%s and categoryID_id=%s' % (provinceID, year,categoryID)
                rows = readFronSqllite(path, sql)
                data = []
                data.append((provinceID, year,categoryID))
                for row in rows:
                    data.append(list(row))
                for i in range(len(data) - 2):
                    data[-(1 + i)][-1] = data[-(1 + i)][-1] - data[-(2 + i)][-1]
                dataset.append(data)
    return dataset

if __name__=="__main__":
    dataset = get_dataset()
    #for data in dataset:
        #print(data)

#dataset形式：[  [ (provinceID,year，categoryID),[分数，人数], [分数，人数]...,[分数，人数] ] , [], []   ]
#data集合了所有数据库中各个省的分数排名信息，由于数据库不完全，后期可能需要进行缺失数据剔除

#9.18版本是分段聚类基本实现，在data中提取一组测试数据testdata，此例为2018年江苏理科数据
testdata=[]
for item in dataset:
    if(item[0]==(4,2018,2)):
        for items in item:
            testdata.append(items)
testdata.remove((4,2018,2))
#print(testdata)

###part2 聚类算法以及其优化


def distance(x, y): #求距离
    return abs(x-y)

def Clustering(data, k):
    #data:分数列表[[分数1， 人数1],...,[分数n， 人数n]] ， k：超参量，簇的数目
    cluster = [] #创建簇中心集合的数组
    belong = []  #记录每一个分数隶属于哪一个中心
    for _ in range(k): #按照k值在cluster中创建代表簇中心数
        cluster.append(data[random.randint(0, len(data)-1)][0])
    for _ in range(len(data)):
        belong.append(-1)  #定义初始值-1表示尚未归属
    while True:
        change = False #标志簇中心是否发生变化
        for index, d in enumerate(data):
            dis = []  #距离列表
            for c in cluster:
                dis.append( distance(d[0], c) )
            if belong[index] != dis.index(min(dis)):
                change = True
                belong[index] = dis.index(min(dis))
        if change == False:
            break
        for index, c in enumerate(cluster):
            sum = 0
            num = 0
            for i, b in enumerate(belong):
                if index == b:
                    sum = sum + (data[i][0] * data[i][1])
                    num = num + data[i][1]
            if num == 0:
                c = 0
            else:
                c = sum/num
                cluster[index] = c
    return cluster,belong

def criterion(data, cluster, belong):
    #data::分数列表[[分数1， 人数1],...,[分数n， 人数n]]
    #cluster:聚类中心数组，长度为k
    #belong:分数隶属中心列表
    k = len(cluster)  # 获取聚类数
    WSS = 0  # WSS:Within cluster sum of squares,表示各个点到cluster中心距离的绝对值,代表误差
    for i in range(0,k):
        for index, b in enumerate(belong):
            if b == i:
                WSS += distance(cluster[i], data[index][0])
    return WSS;

#获取最佳聚类数
maxk = 9 #所测试的最大聚类数
WSSarray = []  # 对聚类数为1,2,...maxk，分别存储其误差值，WSSarray的长度为maxk
for i in range(1,maxk+1):
    cluster, belong = Clustering(testdata, i)
    WSS = criterion(testdata,cluster,belong)
    WSSarray.append(WSS)
# print("不同聚类数对应的误差值所组成的数组为:",WSS)  # 输出误差数组

WSSDelta = list(np.ones(maxk))  # 获得误差数组的增量差，选择增量差最大的点对应的聚类数作为合适的聚类数
WSSDelta[0] = 0
maxDelta = -1
indexDelta = 0
for i in range(1,maxk):
    WSSDelta[i] = WSSarray[i-1] - WSSarray[i]
    if WSSDelta[i]>maxDelta:
        maxDelta = WSSDelta[i]
        indexDelta = i+1  # 较好的聚类数
# print("最大的误差差值为:",maxDelta)  # 输出最大误差
# print("误差差值对应的数组为:",SSEDelta)  # 输出误差差值
#print(WSSDelta)
print("最佳聚类数为:",indexDelta)#输出最佳聚类数

x = list(range(1,maxk+1))
plt.figure()
plt.plot(x, WSSarray)
plt.show()

###此处选取最佳聚类数有两点需要改进或者思考：（1）距离度量的范数（2）拐点的确定
#根据差值，最大拐点往往是k=2，但是从图示可以看出，k=5也可以作为一个较好的拐点进行聚类

x = [d[0] for d in testdata]
y = [d[1] for d in testdata]

###
print('分数列表：',x)

belong1 = Clustering(testdata,2)
print(belong1)

belong2 = Clustering(testdata,5)
print(belong2)


colorlist=[]
for items in belong2[1]:
    if(items==0):
        colorlist.append('grey')
    if(items==1):
        colorlist.append('gold')
    if(items==2):
        colorlist.append('turquoise')
    if(items==3):
        colorlist.append('plum')
    if(items==4):
        colorlist.append('lawngreen')

plt.figure()
plt.xlabel('分数')
plt.ylabel('人数')
plt.bar(x, y, color=colorlist, alpha=0.8)
plt.show()

#最后print出聚类边界和每一个分数的标签，并画出一个分段聚类彩色图(以k=5为例)
#2020.9.18