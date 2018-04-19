from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    #一大堆路由
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)/$', views.detail),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^stusearch/$', views.stusearch),
    url(r'^f/$', views.grades),

    #班级信息路由和学生信息路由
    url(r'^grades/(\d+)/$', views.gradesStudents),
    url(r'^addstudent/$', views.addstudent),

    #显示session属性路由
    url(r'^attri/$', views.att),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),

    url(r'^showregist/$', views.showregist),
    url(r'^showregist/regist/$', views.regist),
    url(r'showresponse/', views.showresponse),

    #重定向路由
    url(r'direct1/', views.redirect1),
    url(r'direct2/', views.redirect2),

    url(r'direct3/', views.redirect3),
    url(r'direct4/', views.redirect4),

    #session会话路由
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain),
    url(r'^quit/$', views.quit),

    #反向解析路由
    url(r'^stu/$', views.stu),
    url(r'^good/(\d+)$', views.good, name='good'),

    #模板继承路由
    url(r'^base/$', views.base),
    url(r'^inhert/$', views.inhert),

    #CSRF
    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo, name='showinfo'),


    #verifycode
    url(r'^vcode/$', views.verifycode, name='vcode'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^verifycheck/$', views.verifycheck, name='verifycheck'),
]