from django.db import models


class Colleges(models.Model):  # 大学类
    collegeID = models.IntegerField(primary_key=True)  # 大学id（主键）
    collegeName = models.TextField()  # 大学名称
    provinceID = models.ForeignKey('Provinces',
                                   on_delete=models.DO_NOTHING,
                                   null=True)  #省份id（外键->Provinces类）
    project985 = models.BooleanField(default=False) #是否为985大学
    project211 = models.BooleanField()#是否为211大学
    top = models.BooleanField() #是否为一流学校
    class Meta:#设置元信息，使用db_table自定义表的名字
        db_table = 'Colleges'
        verbose_name = '大学列表'


class Provinces(models.Model): #省份类
    provinceID = models.IntegerField(primary_key=True) #省份id（主键）
    provinceName = models.TextField() #省份名称
    class Meta:#设置元信息，使用db_table自定义表的名字

        db_table = 'Provinces'
        verbose_name = '省份列表'


class Majors(models.Model): #专业类
    collegeID = models.ForeignKey('Colleges',
                                  on_delete=models.DO_NOTHING,
                                  null=True)#大学id（外键->Colleges类)
    provinceID = models.ForeignKey('Provinces',
                                   on_delete=models.DO_NOTHING,
                                   null=True) #省份id（外键->Provinces类）
    categoryID = models.ForeignKey('Category',
                                   on_delete=models.DO_NOTHING,
                                   null=True) #科类id（外键->Category类）
    majorName = models.TextField()#专业名称
    year = models.IntegerField()
    minScore = models.IntegerField()
    avgScore = models.IntegerField(null=True)#平均分可以为null
    maxScore = models.IntegerField(null=True)#最高分可以为null
    firstlevelIDs = models.TextField(null=True)  # 一级学科（注意这里是文本字段；一个专业可以对应多个一级学科，多个一级学科通过特定符号分开，所以它不是Firstlevel类的外键）
    class Meta:#设置元信息，使用db_table自定义表的名字
        db_table = 'Majors'
        verbose_name = '专业列表'


class Firstlevel(models.Model):#一级学科类
    firstlevelID = models.IntegerField(primary_key=True) # 一级学科id（主键）
    firstlevelName = models.TextField() # 一级学科名称
    subjectID = models.IntegerField() #学科门类id
    subjectName = models.TextField() #学科门类名称
    class Meta:#设置元信息，使用db_table自定义表的名字
        db_table = 'Firstlevel'
        verbose_name = '一级学科'


class Rankings(models.Model):#分数排名类
    provinceID = models.ForeignKey('Provinces',
                                   on_delete=models.DO_NOTHING,
                                   null=True) #省份id（外键->Provinces类）
    categoryID = models.ForeignKey('Category',
                                   on_delete=models.DO_NOTHING,
                                   null=True) #科类id（外键->Category类）
    year = models.IntegerField()
    score = models.IntegerField()
    rank = models.IntegerField()
    class Meta:#设置元信息，使用db_table自定义表的名字
        db_table = 'Rankings'
        verbose_name = '排名列表'


class Category(models.Model):#科类
    categoryID = models.IntegerField(primary_key=True) #科类id（主键）
    categoryname = models.TextField() #科类名称
    class Meta:#设置元信息，使用db_table自定义表的名字
        db_table = 'Category'
        verbose_name = '科类'

