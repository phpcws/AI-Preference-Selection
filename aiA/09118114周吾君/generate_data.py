import json
datas=[]
with open('省份经纬.json','r',encoding='utf8') as f:
    location = json.load(f)
with open('排名.txt','r',encoding='utf8') as f:
    college = f.readlines()
for i in college:
    data={}
    data['college_name']=i.split(',')[2]
    for loc in location:
        if i.split(',')[1] == loc['name']:
            data['college_code']=[loc['value'][0],loc['value'][1]]+[i.split(',')[-1].replace('\n',"")]
            break
    datas.append(data)
with open('college_code.json','w',encoding='utf8') as f:
    json.dump(datas,f)
with open('college_code.json','r',encoding='utf8') as f:
    print(json.load(f))
print(datas)
