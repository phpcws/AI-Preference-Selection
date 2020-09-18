"""
Created on Mon Sep

@author: 李浩天
"""
import scipy.spatial.distance as dist
import numpy as np
import pandas as pd
# import jieba

def JaccardDistance(str1,str2):
    # s1 = set(jieba.cut(str1))
    # s2 = set(jieba.cut(str2))
    s1 = set(str1)
    s2 = set(str2)
    if "(" in s1:
        s1.remove("(")
    if ")" in s1:
        s1.remove(")")
    if "(" in s2:
        s2.remove("(")
    if ")" in s2:
        s2.remove(")")
    intersection = len(list(s1 & s2))
    union = len(list(s1 | s2))
    return intersection / union


if __name__ == '__main__':
    result = pd.read_csv("result.csv")
    standard = pd.read_csv("二级学科改进.csv")

    majors = list(result["Major"][:])
    IDs = list(standard["ID"][:])
    names = list(standard["名称"][:])

    mixed = []
    counts = 0

    for major in majors:
        distances = []

        if major =='all' or major =='All':
            mixed.append("all")
        else:
            for name in names:
                distances.append(JaccardDistance(major, name))
            sim_idx = distances.index(max(distances))
            major_name = names[sim_idx]
            mixed.append(major_name)


            if IDs[sim_idx]<100:
                result["0"][counts] = major_name
            elif 100<IDs[sim_idx]<10000:
                result["1"][counts] = major_name
            else:
                result["2"][counts] = major_name

        counts+=1
        print(counts)

    result["Mixed"] = mixed
    pd.DataFrame.to_csv(result, "test.csv", encoding="UTF-8")

    # 词典(Major1(origin), Major2(disambiguated))
    test = pd.read_csv("test.csv")
    diction = pd.read_csv("dict.csv")
    number = len(test["Major"][:])
    major1 = []
    major2 = []
    diction_pair = []
    for i in range(number):
        diction_pair.append((test["Major"][i], test["Mixed"][i]))

    diction_pair = set(diction_pair)
    print(len(diction_pair))

    for pair in diction_pair:
        major1.append(pair[0])
        major2.append(pair[1])

    diction["major1"] = major1
    diction["major2"] = major2
    pd.DataFrame.to_csv(diction, "dict.csv", encoding="UTF-8")