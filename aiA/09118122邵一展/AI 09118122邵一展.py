#!/usr/bin/env Python
# coding=utf-8
import numpy as np   
import pandas as pd
import random
import os
import csv
import json

csv_data = pd.read_csv('高校录取分数线整合（省份名字统一）.csv')  # 读取数据

college_data = pd.read_csv('大学信息.csv')  # 读取大学数据
college_batch_data = college_data.tail(15)  # 取后15条数据

university = college_batch_data['collegeName'].values.tolist()
universityID = college_batch_data['collegeID'].values.tolist()

#['西北大学', '西安电子科技大学', '长安大学', '兰州大学', '新疆大学', '石河子大学', '青岛大学', '广州大学', 
#'中国矿业大学（北京）', '中国地质大学（北京）', '北京联合大学', '复旦大学医学部', '重庆大学', '中国科学技术大学', '浙江工业大学']

Year = [2017,2018,2019]
Province = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江',
    '安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川',
    '贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆','香港','澳门','台湾']
category = ["文科","理科", "all"]

result = open("09118122邵一展.csv","w",encoding="utf-8-sig",newline='')
writer=csv.writer(result)
writer.writerow(["rank","province","category","college"])

addition = 20 #向上浮动的分值
for u in university:
    for y in Year:
        for p in Province:
            for c in category:
                temp_data = csv_data.loc[(csv_data["College"] == u) & (csv_data["Province"] == p) &
                                        (csv_data["Year"] == y) & (csv_data["category"] == c), 
                                        ["College", "Year" , "Province", "category","score"]]

                if not temp_data.empty: #存在dataframe
                    score_list = temp_data["score"].values.tolist()
                    score_list.sort()
                    low_score = score_list[0] #录取最差专业的最低分，如xx的录取最低分
                    high_score = score_list[-1] + addition #录取最好专业的最低分加上向上浮动的分值，如AI的录取最低分
                    if c == "all":
                        temp = "json/" + str(y) + p + "all" + ".json" 
                    else:
                        temp = "json/" + str(y) + p + c + ".json" 

                    if os.path.exists(temp):
                        with open(temp,'r',encoding='UTF-8') as load_f:
                            load_dict = json.load(load_f)
                            if (str(low_score) in load_dict[str(y)][p][c]) & (str(high_score) in load_dict[str(y)][p][c]):
                                low_rank = load_dict[str(y)][p][c][str(low_score)]
                                high_rank = load_dict[str(y)][p][c][str(high_score)]
                                number = (low_rank-high_rank) // 20 + 1 #至少一名，整除30代表近似该分数段有20/88的学生去该大学
                                for _ in range(number):
                                    random_score = random.randint(low_score, high_score) #产生随机分数
                                    if (str(random_score) in load_dict[str(y)][p][c]):
                                        random_rank = load_dict[str(y)][p][c][str(random_score)]
                                    else: 
                                        random_rank = 1 #说明random_score超过了一分一段表的最高分
                                    writer.writerow([random_rank, p, c, u])
                            else:
                                for _ in range(10):     #假设10人
                                    writer.writerow(["null", p, c, u])  #null代表存在相应的json但没有对应的分，需要人工进行数据模拟

                    else:
                        for _ in range(20):     #假设20人
                            writer.writerow(["nan", p, c, u])  #nan代表不存在相应的json，也需要人工进行数据模拟
