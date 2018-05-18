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

#template
def stu(request):
    stulist = Students.stuObj.all()
    # return render(request, 'myApp/good.html')
    return render(request, 'myApp/stu.html',  {'students':stulist, 'list': ['a', 'b', 'c'], 'test': '我是test', 'num':80})

def good(request, id):
    return render(request, 'myApp/good.html', {'students':[], 'num':id})

#模板继承
def base(request):
    return render(request, 'myApp/base.html')

def inhert(request):
    return render(request, 'myApp/inhertit.html')


def postfile(request):
    return render(request, 'myApp/post.html')

def showinfo(request):
    name = request.POST['username']
    pwd = request.POST['passwd']
    return render(request, 'myApp/showinfo.html', {'username':name, 'passwd':pwd})


def verifycode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random

    bgcolor = (random.randrange(20, 100), random.randrange(20, 100),
               random.randrange(20, 100))
    width = 150
    height = 50

    im = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    font = ImageFont.truetype(r'C:\Windows\Fonts\ROCK.TTF', 40)
    colors = []
    pos = [5, 25, 50, 75]
    ins = 0
    for i in range(4):
        colors.append((255, random.randrange(0, 255), random.randrange(0, 255)))
    for s, color in zip(rand_str, colors):
        draw.text((pos[ins], 2), s, font=font, fill=color)
        ins += 1
    print(rand_str)
    del draw
    request.session['vfcode'] = rand_str
    import io
    buf = io.BytesIO()
    im.save(buf, 'png')

    return HttpResponse(buf.getvalue(), 'img/png')

def verify(request):
    f = request.session.get('flag')
    string = ''
    if f == False:
        string = "请重新输入"
    request.session.clear()
    return render(request, 'myApp/verifycodefile.html', {'flag':string})

def verifycheck(request):
    raw = request.POST['verifycode'].upper()
    code = request.session['vfcode'].upper()

    if raw == code:
        return render(request, 'myApp/success.html')
    else:
        request.session['flag'] = False
        return redirect(to='/sun/verify/')

def indexcss(request):
    return render(request, 'myApp/index_css.html')


#文件上传
def upfile(request):
    return render(request, 'myApp/upfile.html')


import os
from django.conf import settings
def savefile(request):
    if request.method == 'POST':
        f = request.FILES['file']
        #合成文件在服务器端得到路径
        filePath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filePath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败！')


from django.core.paginator import Paginator
def page(request, id):
    stulist = Students.stuObj.all()
    page_num = 6
    page = Paginator(stulist, page_num)
    page_list = page.page(id)
    return render(request, 'myApp/studentsPage.html', {'stulist':page_list})

def ajaxstudent(request):
    stu = Students.stuObj.all()
    return render(request, 'myApp/ajaxstudents.html')

from django.http import JsonResponse
def studentsinfo(request):
    stu = Students.stuObj.all()
    list = []
    for stu in stu:
        list.append([stu.sname, stu.sage])
    return JsonResponse({"data":list})


#富文本
def edit(request):
    return render(request, 'myApp/edit.html')


import time
def celery(request):
    print("uio")
    time.sleep(5)
    print("uio")

    return render(request, 'myApp/celery.html')