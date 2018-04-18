from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)/$', views.detail),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^stusearch/$', views.stusearch),
    url(r'^f/$', views.grades),

    url(r'^grades/(\d+)/$', views.gradesStudents),
    url(r'^addstudent/$', views.addstudent),

    url(r'^attri/$', views.att),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),

    url(r'^showregist/$', views.showregist),
    url(r'^showregist/regist/$', views.regist),
    url(r'showresponse/', views.showresponse),

    url(r'direct1/', views.redirect1),
    url(r'direct2/', views.redirect2),

    url(r'direct3/', views.redirect3),
    url(r'direct4/', views.redirect4),

    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain),
    url(r'^quit/$', views.quit),
]