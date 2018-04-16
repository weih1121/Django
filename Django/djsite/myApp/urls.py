from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.index)
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)/$', views.detail),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^stusearch/$', views.stusearch),
    url(r'^f/$', views.grades),

    url(r'^grades/(\d+)$', views.gradesStudents),
    url(r'^addstudent$', views.addstudent),
]