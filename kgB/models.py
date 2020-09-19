from django.db import models
from py2neo import Graph, Node, Relationship
from rec2020.settings import graph

# Create your models here.

def get_985s():
    query = "match (n:`学校`) where n.`_985_`=1 return n"
    colleges_985 = graph.run(query)
    return colleges_985

def getProvinceID(province):
    """
    get province ID
    :param province: province string; e.g.: '河南'
    :return: int ID; e.g.: 1
    """
    query = "match (n:`省份`) where n.Name='" + str(province)+ "' return n"
    resultDict = dict(graph.run(query).data()[0]['n'])
    return resultDict['ID']

def get_collegesInProvince(province):
    """
    get colleges in target province
    :param province: province string; e.g.: '河南'
    :return: a list of college info dict
    """
    query = "MATCH (n:`学校`)-[:located]-(p:`省份`) WHERE p.Name='" + str(province)+ "' RETURN n"
    collegesInProvince = []
    result = graph.run(query).data()
    for item in result:
        collegesInProvince.append(dict(item['n']))
    return collegesInProvince

def get_nodelist(province):
    """
    get nodes (college only 985)
    :param province: province string; e.g.: '河南'
    :return: a list of node
    """
    nodelist = []
    # append college nodes
    collegelist = get_collegesInProvince(province)
    for item in collegelist:
        if item['_985_']:
            nodelist.append(
                {'data': {'id': str(item['ID']), 'name': item['Name'], 'label': 'college'}}
            )
    # append province node
    nodelist.append({'data': {'id': str(getProvinceID(province)), 'name': province, 'label': 'province'}})
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