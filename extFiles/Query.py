import pandas as pd
import time
import os


# 接收大学，科类，年份，省份为输入参数，展示大学该年份在该省的各专业分数情况及排名
def query_1(college, Category, year, Province):  # year必须是自然数，in17，18，19
    """
    college:是大学名称
    Category:是科类，是{"理科","文科","不分文理"}
    year:年份只能是2019，2018，2017，应该是数字类型
    province:省份名称
    """
    table = pd.read_csv(f"final_{year}.csv")#这个地方是文件名称，可能要改
    #table=pd.read_csv('D:\大三短学期课程\软件实践2\my_work\iseu2012-rec2020-master\\rec2020\extFiles\\final_2018.csv')
    table.columns = ["College", "Year", "Province", "Category", "Major", "Score"]  # 加入标题行
    tar_major = []
    tar_score = []
    for item in table.iterrows():
        if item[1][0] == college and item[1][2] == Province and item[1][3] == Category:
            tar_major.append(item[1][4])
            tar_score.append(item[1][5])
    Data = {"Major": tar_major,
            "Socre": tar_score}
    Data_f = pd.DataFrame(Data)

    return Data_f
start=time.time()
res1=query_1('东南大学','理科',2018,'山西')#大约8s
print(res1)
end=time.time()
print(f'1号查询花费时间{end-start}s')
print("#######################################################################")
#查询某年某省某类别的一分一段表，我们在数据集的名称上进行了微调
def score_iqury(Year,Category,Province):
    """
    是用来展示一分一段表的,我们将一分一段表的奇怪后缀去掉了，如果是all，则category设置为all即可
    Year:年份只能是2019，2018，2017，应该是数字类型
    Category:是科类，是{"理科","文科","不分文理"}
    province:省份名称
    """
    year=str(Year)
    name=year+Province+Category
    path="json_csv//"+name+".csv"
    df1=pd.read_csv(path)
    df2=df1.drop(['Unnamed: 0','省份','年份','科类'],axis=1)
    return df2

start=time.time()
res2=score_iqury(2018,'理科','山西')
print(res2)
end=time.time()
print(f'一分一段表号查询花费时间{end-start}s')
print("#######################################################################")

#接收的输入为分数，省份，科目类别，这个输入的年份应自动标记为当前年份，用以看去年的分数情况,分数上下波动10分
def query_2(score,province,category,year=2020,wave=10):
    """
    这个用来展示用户分数在去年上下波动10分有哪些选择的情况。
    wave:是分数上下波动所允许的范围
    """
    #table = pd.read_csv(f"final_{year}.csv")  # 这个地方是文件名称，可能要改
    table=pd.read_csv('D:\大三短学期课程\软件实践2\my_work\iseu2012-rec2020-master\\rec2020\extFiles\\final_2018.csv')
    table.columns=["College","Year","Province","Category","Major","Score"]#加入标题行
    tar_major=[]
    tar_score=[]
    tar_college=[]
    tar_province=[]
    for item in table.iterrows():
        if item[1][5]<=score+wave and item[1][5]>=score-wave and item[1][2]==province and item[1][3]==category:
            tar_major.append(item[1][4])
            tar_score.append(item[1][5])
            tar_college.append(item[1][0])
            tar_province.append(item[1][2])
    Data={"College":tar_college,"Major":tar_major,
     "Socre":tar_score,'Province':tar_province}
    Data_f=pd.DataFrame(Data)
    return Data_f

start=time.time()
res3=query_2(625,'山西','理科',2019)
print(res3)
end=time.time()
print(f'2号查询查询花费时间{end-start}s')
print("#######################################################################")


