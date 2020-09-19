import numpy as np
import pandas as pd

data = pd.read_csv('./extFiles/高校录取分数线整合.csv', encoding='utf-8')
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
new_data = pd.DataFrame(columns=['College', 'Year', 'Province', 'category', 'Major', 'score', 'Contributor'])

colleges = []
years = [2017, 2018, 2019]
provinces = ['安徽', '北京', '福建', '广东', '广西', '贵州', '河北', '河南', '黑龙江', '湖北', '湖南', '吉林',
            '江苏', '辽宁', '内蒙古', '宁夏', '青海', '山东', '山西', '上海', '四川', '天津', '云南', '浙江',
            '重庆', '海南', '新疆']
categories = ['文科', '理科', '不分文理']

for item in data['College'].values:
    if '\ufeff' in item:
        item = item.replace('\ufeff', '')
    if item not in colleges:
        colleges.append(item)

for year in years:
    y_data = data.loc[data['Year'] == year]
    for college in colleges:
        if college not in y_data['College'].values:
            continue
        else:
            c_data = y_data.loc[y_data['College'] == college]
            for province in provinces:
                if province not in c_data['Province'].values:
                    continue
                else:
                    p_data = c_data.loc[c_data['Province'] == province]
                    for m_category in categories:
                        if m_category not in p_data['category'].values:
                            continue
                        else:
                            final_data = p_data.loc[p_data['category'] == m_category]
                            final_data = final_data[final_data['score'] > 330]
                            if final_data.empty:
                                continue
                            else:
                                row = final_data['score'].idxmin()
                                print(data.iloc[row, :])
                                new_data = new_data.append(data.iloc[row, :])


new_data.to_csv('min_score2.csv', encoding='utf-8-sig')













