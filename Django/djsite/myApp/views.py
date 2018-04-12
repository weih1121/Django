from django.shortcuts import render
from .models import Grades, Students

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def detail(request, num, num1):
    return HttpResponse("num + num1 = %s"%(num + num1))

def grades(request):
    #去模型取数据
    gradeslist =  Grades.objects.all()
    #将数据传递给模板， 模板再渲染页面， 将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {"grades": gradeslist}) #"grades"模板中的对象

def students(request):
    studentList = Students.objects.all()
    return render(request, 'myApp/students.html', {"students": studentList})

def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students': studentsList})
