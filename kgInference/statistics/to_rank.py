import numpy as np
import pandas as pd
import os
import json

data = pd.read_csv('min_score2.csv', encoding='utf-8')

data.rename(columns={'Contributor': 'Ranking'}, inplace=True)

data['Ranking'] = np.nan

path = "./一分一段/"
files = os.listdir(path)

for file in files:
    position = path + file
    with open(position, 'r', encoding='utf-8') as f:
        dic = json.load(f)
        for k1, v1 in dic.items():
            print(k1)
            for k2, v2 in v1.items():
                print(k2)
                for k3, v3 in v2.items():
                    print(k3)
                    if k3 == 'all':
                        new_data = data.loc[(data['Year'] == int(k1)) & (data['Province'] == k2)]

                        for index, row in new_data.iterrows():
                            m_score = row['score']
                            m_school = row['College']
                            m_cate = row['category']
                            m_score_str1 = str(m_score)
                            m_score_str2 = m_score_str1 + '.0'

                            if m_score_str1 in v3.keys():
                                m_rank = v3[m_score_str1]

                                data.loc[(data['Year'] == int(k1)) & (data['Province'] == k2) & (
                                        data['category'] == m_cate) & (data['College'] == m_school), 'Ranking'] = m_rank

                            elif m_score_str2 in v3.keys():
                                m_rank = v3[m_score_str2]

                                data.loc[(data['Year'] == int(k1)) & (data['Province'] == k2) & (
                                        data['category'] == m_cate) & (data['College'] == m_school), 'Ranking'] = m_rank
                            else:
                                continue

                    else:
                        new_data = data.loc[(data['Year'] == int(k1)) & (data['Province'] == k2) & (data['category'] == k3)]
                        for index, row in new_data.iterrows():
                            m_score = row['score']
                            m_school = row['College']
                            m_score_str1 = str(m_score)
                            m_score_str2 = m_score_str1 + '.0'

                            if m_score_str1 in v3.keys():
                                m_rank = v3[m_score_str1]

                                data.loc[(data['Year'] == int(k1)) & (data['Province'] == k2) & (
                                        data['category'] == k3) & (data['College'] == m_school), 'Ranking'] = m_rank

                            elif m_score_str2 in v3.keys():
                                m_rank = v3[m_score_str2]

                                data.loc[(data['Year'] == int(k1)) & (data['Province'] == k2) & (
                                        data['category'] == k3) & (data['College'] == m_school), 'Ranking'] = m_rank
                            else:
                                continue

print(data)

data.to_csv('名次-高校.csv', encoding='utf-8-sig')






