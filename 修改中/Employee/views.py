from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Employee import models
from department import models1
from django.contrib.auth import login, logout, authenticate  # 登录，推出，验证
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import datetime


# Create your views here.
@login_required
def employee1(request):
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    em = models.Employeeinfo.objects.get(employ_id=employ.id)
    dep = models1.DepartMent.objects.get(id=employ.departms_id)
    context = {
        'aaa': 'active',
        'user': user,
        'employ': employ,
        'em': em,
        'dep': dep,
    }
    return render(request, 'Employee/myinfo.html', context)


@login_required
def fanhui(request):
    return render(request, 'home/Employeeinfo.html')


# 假期申请信息添加
# @login_require
@login_required
def application_add(request):
    if request.method == 'POST':
        a = request.POST.get('Applidate', None)
        b = request.POST.get('EmployeeNum', None)
        c = request.POST.get('AppliType', None)
        d = request.POST.get('BeginTime', None)
        e = request.POST.get('EndTime', None)
        f = request.POST.get('Days', None)
        g = request.POST.get('Reason', None)
        i = request.POST.get('ConfirmName', None)
        Em = models.UserProfil.objects.get(EmployeeNum=b)
        models.LeaveApplication.objects.create(Applidate=a, EmployeeNum=b, AppliType=c, BeginTime=d, EndTime=e,
                                               Days=f, Reason=g, ConfirmName=i, Em_id=Em.id)
        return HttpResponseRedirect('department1')
    else:
        time = datetime.datetime.now()
        resss = models.LeaveApplication.objects.all()
        context = {
            'ccc': 'active',
            'time': time,
            'resss': resss
        }
        return render(request, 'Employee/application.html', context)


# def change(request):

# 退出
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login')


@login_required
def search(request):
    user = User.objects.get(id=request.user.id)
    Em = models.UserProfil.objects.get(user_id=user.id)
    emnum = models.LeaveApplication.objects.filter(EmployeeNum=Em.EmployeeNum).all()
    context = {
        'sss': 'active',
        'emnum': emnum
    }
    return render(request, 'home/search.html', context)


# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        nick = request.POST.get('nick', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        employee = request.POST.get('employee', None)
        department = request.POST.get('department', None)
        type = request.POST.get('type', None)
        if username and password1 and password2:
            if password1 == password2:
                u_count = User.objects.filter(username=username).count()
                if u_count == 0:  # 没有这个用户名
                    # 用户自带表
                    user_info = {
                        'username': username,
                        'email': email,
                        'password': make_password(password1),
                    }
                    user_info1 = User.objects.create(**user_info)
                    if type == '部门负责人':
                        tms = models1.DepartMent.objects.get(DepartMentStaffNum=employee)
                    else:
                        tms = models1.DepartMent.objects.get(DepartMentName=department)
                    # 添加用户扩展信息
                    user_profil = {
                        'nick': nick,
                        'Phone': phone,
                        'UserType': type,
                        'user': user_info1,
                        'EmployeeNum': employee,
                        'departms': tms
                    }
                    models.UserProfil.objects.create(**user_profil)
                    return HttpResponseRedirect('/user_login')
                else:  # 用户已存在
                    return render(request, 'home/reg.html', {'errer': '用户名已存在'})
            else:
                return render(request, 'home/reg.html', {'errer': '两次密码不一样，请重新输入'})
        # 对注册信息做校验
    else:
        s = models1.DepartMent.objects.all()
        context = {
            's': s,
        }
        return render(request, 'home/reg.html', context)


# 登录
def user_login(request):
    if request.method == 'POST':
        a = request.POST.get('username', None)
        b = request.POST.get('password', None)
        c = request.POST.get('posts', None)
        user = models.User.objects.get(username=a)
        types = models.UserProfil.objects.get(user_id=user.id)
        if a and b:
            users = authenticate(username=a, password=b)
            if users is not None:
                if users.is_active:
                    if c == types.UserType and types.UserType == '普通员工':
                        login(request, users)
                        return HttpResponseRedirect('/Employee')
                    elif c == types.UserType and types.UserType == '部门负责人':
                        login(request, users)
                        return HttpResponseRedirect('/department')
                else:
                    return render(request, 'home/login.html', {'errer': '账号已被冻结'})
            else:
                return render(request, 'home/login.html', {'errer': '用户名或密码错误'})
    else:
        return render(request, 'home/login.html')


def manage(request):
    context = {
        'manage': 'active'
    }
    return render(request, 'home/manage.html', context)


@login_required
def myhistoappli(request):
    user = User.objects.get(id=request.user.id)
    Em = models.UserProfil.objects.get(user_id=user.id)
    emnum = models.LeaveApplication.objects.filter(EmployeeNum=Em.EmployeeNum).all()
    context = {
        'zzz': 'active',
        'emnum': emnum
    }
    return render(request, 'Employee/myhistoappli.html', context)
