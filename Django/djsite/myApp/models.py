from django.db import models

# Create your models here.


#对应数据库里的一张表
class Grades(models.Model):
    #模型类里的属性对应数据库里的字段
    gname = models.CharField(max_length=20, db_column="班级名")
    gdate = models.DateTimeField(db_column="创建时间")
    ggirlnum = models.IntegerField(db_column="女生数量")
    gboynum = models.IntegerField(db_column="男生数量")
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

    class Meta:
        db_table  = "grades"
        ordering = ["id"]


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    def createStudent2(self, name, age, gender, contend,
                      grade, last, Create, isD=False):
        student = self.model()
        student.sname = name
        student.sage = age
        student.sgender = gender
        student.scountend = contend
        student.sgrade = grade
        student.lastTime = last
        student.createTime = Create
        return student

class Students(models.Model):

    # 定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, age, gender, contend,
                      grade, last, Create, isD=False):
        student = cls(sname=name, sage=age, sgender=gender, scountend=contend,
                      sgrade=grade, lastTime=last, createTime=Create, isDelete=isD)
        return student

    #自定义模型管理器
    stuObj = StudentsManager()
    sname = models.CharField(max_length=20, db_column="姓名")
    sgender = models.BooleanField(default=True, db_column="性别")
    sage = models.IntegerField(db_column="年龄")
    scountend = models.CharField(max_length=20, db_column="描述")
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE, db_column="班级")            #关联外键

    def __str__(self):
        return self.sname

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "students"
        ordering = ['id']


from  tinymce.models import HTMLField
class Text(models.Model):
    str = HTMLField()

