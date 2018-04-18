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

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华", 34, True, "我叫刘德华",
                                 grade, "2018-4-15", "2018-4-15")
    stu.save()
    return HttpResponse("添加成功")


def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj.createStudent2("张学友", 55, True,
                                        "我叫张学友", grade, "2018-4-15", "2018-4-15")
    stu.save()
    return HttpResponse("添加成功")

def students(request):
    studentList = Students.stuObj.all()
    return render(request, 'myApp/students.html', {"students": studentList})


#报异常
def students2(request):
    studentList = Students.stuObj.get(sgender=True)
    return HttpResponse("----====-----")

def students3(request):
    studentList = Students.stuObj.all()[0:4]
    return render(request, 'myApp/students.html',
                  {'students': studentList})


#分页显示学生
def stupage(request, page):
    studentsList = []
    if page == 0:
        return render(request, 'myApp/students.html',
                      {'students': studentsList})
    studentsList = Students.stuObj.all()[(int(page) - 1) * 5:int(page) * 5]
    return render(request, 'myApp/students.html',
                  {'students': studentsList})


def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students': studentsList})

from django.db.models import Max, Min, Sum, Avg, Count, F, Q
def stusearch(request):
    # studentList = Students.stuObj.filter(sname__contains="数")
    # studentList = Students.stuObj.filter(sname__startswith="风")
    # studentList = Students.stuObj.filter(sname__endswith="堂")
    # studentList = Students.stuObj.filter(pk__in=[2, 4, 6, 8, 9])
    # studentList = Students.stuObj.filter(pk__gte=5)
    # studentList = Students.stuObj.filter(lastTime__day=16)
    # studentList = Students.stuObj.filter(sname__contains="艾")
    # studentList = Students.stuObj.filter(scountend__contains="刘德华")
    # maxAge = Students.stuObj.aggregate(Count('sage'))
    # print(maxAge)
    # return render(request, 'myApp/students.html', {'students': studentList})
    #跨关联查询
    #描述中带有张学友的数据时属于哪个班级的
    grade = Grades.objects.filter(students__scountend__contains="张学友")
    print(grade)
    return HttpResponse('========++++=======')


def grades(request):
    # g = Grades.objects.filter(ggirlnum__gt=F('gboynum') + 100)
    # print(g)
    stu = Students.stuObj.filter(Q(pk__lte = 3) | Q(sage__gt=50))
    return render(request, 'myApp/students.html', {'students': stu})


def att(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.environ)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.path)
    print(request.session)

    return HttpResponse("attributes")

#GET
def get1(request):
    # a = request.GET.get('a')
    a = request.GET['a']
    b = request.GET.get('b')
    c = request.GET.get('c')

    return HttpResponse(a + " " + b + ' ' + c)

def get2(request):
    a = request.GET.getlist('a')
    return HttpResponse(a)

#POST
def showregist(request):
    return render(request, 'myApp/regist.html')

def regist(request):
    # name = request.POST['name']
    name = request.POST.get('name')
    gender = request.POST['gender']
    age = request.POST['age']
    hobby = request.POST.getlist('hobby')

    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("注册成功")


#response
def showresponse(request):
    res = HttpResponse()
    res.content = b'code'
    print(res.charset)
    print(res.content)
    print(res.status_code)
    return res

from django.http import HttpResponseRedirect
#重定向
def redirect1(request):
    return HttpResponseRedirect('/sun/direct2')

def redirect2(request):
    return HttpResponse("重定向后的视图2")

#重定向简写版
from django.shortcuts import redirect
def redirect3(request):
    return redirect(to='/sun/direct4/')

def redirect4(request):
    return HttpResponse("重定向后的视图4")


#session
def main(request):
    #取session
    username = request.session.get('username', '游客')
    return render(request, 'myApp/main.html',
                  {'username':username})


def login(request):
    return render(request, 'myApp/login.html')


def showmain(request):
    username = request.POST.get('username')
    #存储session
    request.session['username'] = username
    return redirect(to='/sun/main/')

from django.contrib.auth import logout
def quit(request):
    #清除session
    # logout(request)   #method 1
    # request.session.clear()   #method 2
    request.session.flush() #method 3
    return redirect(to='/sun/main/')