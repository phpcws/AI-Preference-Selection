from django.db import models
from py2neo import Graph, Node, Relationship, NodeMatcher
from rec2020.settings import graph

# Create your models here.

def get_provinceID(province):
    """
    获取省份ID
    :param province: 省份, string; 例如: '河南'
    :return: 省份ID, int; 例如: 1
    """
    query = "match (n:`省份`) where n.Name='" + str(province)+ "' return n"
    resultDict = dict(graph.run(query).data()[0]['n'])
    return resultDict['ID']

def get_collegesInProvince(province):
    """
    获取特定省份内的大学列表
    :param province: 省份, string; 例如: '河南'
    :return: 一个 大学信息字典 的列表
    """
    query = "MATCH (n:`学校`)-[:located]-(p:`省份`) WHERE p.Name='" + str(province)+ "' RETURN n"
    collegesInProvince = []
    result = graph.run(query).data()
    for item in result:
        collegesInProvince.append(dict(item['n']))
    return collegesInProvince

def get_nodelist(province):
    """
    获取特定省份的节点列表（用于知识图谱可视化）
    注：此处只获取了省内211院校，而非全部
    :param province: 省份, string; 例如: '河南'
    :return: 结点列表
    """
    nodelist = []
    # append college nodes
    collegelist = get_collegesInProvince(province)
    for item in collegelist:
        if item['_211_']:
            nodelist.append(
                {'data': {'id': str(item['ID']), 'name': item['Name'], 'label': 'college'}}
            )
    # append province node
    nodelist.append({'data': {'id': str(get_provinceID(province)), 'name': province, 'label': 'province'}})
    # append scoreinfo nodes
    nodelist.append({'data': {'id': '2017w', 'name': '2017文', 'label': 'scoreinfo'}})
    nodelist.append({'data': {'id': '2017l', 'name': '2017理', 'label': 'scoreinfo'}})
    nodelist.append({'data': {'id': '2018w', 'name': '2018文', 'label': 'scoreinfo'}})
    nodelist.append({'data': {'id': '2018l', 'name': '2018理', 'label': 'scoreinfo'}})
    nodelist.append({'data': {'id': '2019w', 'name': '2019文', 'label': 'scoreinfo'}})
    nodelist.append({'data': {'id': '2019l', 'name': '2019理', 'label': 'scoreinfo'}})
    return nodelist

def get_relationshiplist(nodelist):
    college_list = []
    scoreinfo_list = []
    for item in nodelist:
        label = item['data']['label']
        if (label == 'college'):
            college_list.append(item)
        elif label == 'province':
            provinID = item['data']['id']
        elif label == 'scoreinfo':
            scoreinfo_list.append(item)
    relationshiplist = []
    for item in college_list:
        relationshiplist.append({'data': {'source': str(item['data']['id']), 'target': str(provinID), 'relationship':'located'}})
    for item in scoreinfo_list:
        relationshiplist.append({'data': {'source': str(item['data']['id']), 'target': str(provinID), 'relationship':'score_province'}})
    return relationshiplist

def get_provincedict():
    """
    获得 省份ID-省份 的对应字典
    :return: 省份ID-省份 字典, dict; 例如:{"1": "北京", "2": "天津", "3":"江苏"}
    """
    query = "MATCH (n:`省份`) RETURN n"
    data = graph.run(query).data()
    provincedict = dict()
    for item in data:
        d = dict(item['n'])
        provincedict[str(d['ID'])] = d['Name']
    return provincedict

def get_ranktable(provinceID, year, category):
    """
    获取一分一段表
    :param provinceID: 省份编号, int
    :param year: 年份, int
    :param category: 科类, string
    :return: 一分一档字典, dict; 例如:{700: 20, 695: 26, 690: 38, 685: 50, ...}
    """
    matcher = NodeMatcher(graph)
    data = matcher.match("分数信息",
        provinceID=provinceID,
        year=year,
        category=category).all()[0]
    scoreinfo = dict(data)
    if(len(scoreinfo['score']) != len(scoreinfo['cumulateNumber'])):
        raise IndexError
    ranktable = dict()
    for score, rank in zip(scoreinfo['score'], scoreinfo['cumulateNumber']):
        ranktable[score] = rank
    return ranktable