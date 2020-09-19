import sqlite3 as db

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
            sql = 'select score,rank from Rankings where provinceID_id=%s and year=%s' % (provinceID, year)
            rows = readFronSqllite(path, sql)
            data = []
            data.append((provinceID, year))
            for row in rows:
                data.append(list(row))
            for i in range(len(data) - 2):
                data[-(1 + i)][-1] = data[-(1 + i)][-1] - data[-(2 + i)][-1]
            dataset.append(data)
    return dataset

if __name__=="__main__":
    dataset = get_dataset()
    for data in dataset:
        print(data)

#dataset形式：[  [ (provinceID,year),[分数，人数], [分数，人数]...,[分数，人数] ] , [], []   ]