from django.contrib import admin

# Register your models here.
from .models import Grades, Students


class StudentInfo(admin.TabularInline):
    model = Students
    extra = 2

#注册
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):    #GradeAdmin新的管理页面
    inlines = [StudentInfo]
    # list_display = ['pk', 'gname']
    #列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gdate', 'ggirlnum', 'gboynum']
    search_fields = ['gdate']
    list_per_page = 3

    #
    # #添加，修改页属性
    #fields = ['isDelete', 'gname', 'gdate', 'ggirlnum', 'gboynum']               #规定属性先后顺序
    fieldsets = [
        ("num", {"fields" : ['ggirlnum', 'gboynum']}),
        ("base", {"fields" : ['gname', 'gdate', 'isDelete']})
    ]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):  # GradeAdmin新的管理页面

    def gender(self):
        if self.sgender:
            return '男'
        return '女'
    #设置页面列的名称
    gender.short_description =  "性别"

    def isdelete(self):
        if self.isDelete:
            return 1
        return 0

    isdelete.short_description = "删除"
    # 列表页属性
    list_display = ['pk', 'sname', gender, 'sage', 'scountend', isdelete, 'sgrade']

    list_filter = ['sname', 'sgender']
    search_fields = ['pk']
    list_per_page = 3
    #

    #
    # #添加，修改页属性
    # fields = []
    fieldsets = [
        ("num" , {"fields" : ['sname', 'sage']}),
        ("other", {"fields" : [ 'sgender', 'scountend',  'isDelete', 'sgrade']})
    ]

    #执行动作位置
    actions_on_bottom = True
    actions_on_top = False

#admin.site.register(Grades, GradesAdmin)       #要将表注册到自定义的管理界面，才能用到那个表
#admin.site.register(Students, StudentsAdmin)
