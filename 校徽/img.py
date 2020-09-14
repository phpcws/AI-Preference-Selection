import pandas as pd
import numpy as np
import os
import shutil

def scan_files(directory,prefix=None,postfix=None):
    files_list=[]
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))
               
    return files_list


names=pd.read_excel('names.xlsx')
names=names['分配高校']
names=names.to_list()
files=scan_files('all_img')
result=[]

for i in range(len(names)):
    names[i]=names[i]+'.jpg'
    names[i]='all_img\\'+names[i]
    if names[i] in files:
        result.append(names[i][8:])

for i in range(len(result)):
    shutil.copyfile('all_img\\'+result[i],'result_img\\'+result[i])