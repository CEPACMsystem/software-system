from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate #登录，推出，验证
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from department import models1
from Employee import models
# Create your views here.

@login_required
def department1(request):
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    dep = models1.DepartMent.objects.get(id=employ.departms_id)
    context = {
        'ddd': 'active',
        'user': user,
        'employ': employ,
        'dep': dep,
    }
    return render(request, 'department/emappliinfo.html', context)
@login_required
def emappliinfo(request):
    applications = []
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    employees = models.Employeeinfo.objects.filter(mde_id=employ.departms_id).all()
    for a in employees:
        b = models.LeaveApplication.objects.filter(ConfirmLogo__isnull=True,ConfirmName=a.EmployeeName).all()
        applications.append(b)
    context = {
        'eee':'active',
        'applications':applications
    }
    return render(request,'department/applications1.html',context)
@login_required
def noagree(request):
    a = '未同意'
    res = request.GET.get('eid', None)
    models.LeaveApplication.objects.filter(pk=res).update(ConfirmLogo = a)
    return HttpResponseRedirect('/department/emappliinfo')

#管理员批准功能
@login_required
def agree(request):
    a = '同意'
    res = request.GET.get('eid', None)
    models.LeaveApplication.objects.filter(pk=res).update(ConfirmLogo = a)
    return HttpResponseRedirect('/department/emappliinfo')

#请假历史信息
@login_required
def historyappli(request):
    applications = []
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    employees = models.Employeeinfo.objects.filter(mde_id=employ.departms_id).all()
    for a in employees:
        b = models.LeaveApplication.objects.filter(ConfirmLogo__isnull=False, ConfirmName=a.EmployeeName).all()
        applications.append(b)
    context = {
        'fff':'active',
        'applications':applications
    }
    return render(request,'department/hisappliinfo.html',context)
@login_required
def employeeinfo(request):
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    employees = models.Employeeinfo.objects.filter(mde_id=employ.departms_id).all()
    context = {
        'aaa': 'active',
        'employees': employees
    }
    return render(request,'home/Employeeinfo.html',context)

#添加员工信息业务
@login_required
def employee_add(request):
    if request.method == 'POST':
        a = request.POST.get('EmployeeNum', None)
        b = request.POST.get('EmployeeName', None)
        c = request.POST.get('StaffNum', None)
        d = request.POST.get('depart',None)
        employ = models.UserProfil.objects.get(EmployeeNum=a)
        mde = models1.DepartMent.objects.get(DepartMentName=d)
        models.Employeeinfo.objects.create(EmployeeNum=a, EmployeeName=b, StaffNum=c, DepartmentNum=d, employ_id=employ.id,mde=mde)
        return HttpResponseRedirect('/department')
    else:
        user = User.objects.get(id=request.user.id)
        employ = models.UserProfil.objects.get(user_id=user.id)
        departs = models1.DepartMent.objects.get(id = employ.departms_id)
        context = {
            'bbb': 'active',
            'departs': departs
        }
        return render(request,'Employee/employee_add.html',context)

#修改
@login_required
def employee_change(request):
    res = request.GET.get('eid', None)
    if request.method == 'POST':
        a = request.POST.get('EmployeeNum', None)
        b = request.POST.get('EmployeeName', None)
        c = request.POST.get('StaffNum', None)
        d = request.POST.get('DepartmentNum',None)
        models.Employeeinfo.objects.filter(pk=res).update(EmployeeNum=a, EmployeeName=b, StaffNum=c, DepartmentNum=d)
        return HttpResponseRedirect('/department')
    else:
        res = request.GET.get('eid',None)
        em = models.Employeeinfo.objects.get(pk=res)
        departes = models1.DepartMent.objects.all()
        return render(request,'Employee/employ_change.html',{'em':em,'departes':departes})

#员工信息删除业务
@login_required
def employee_del(request):
    res = request.GET.get('eid',None)
    if res is not None:
        models.Employeeinfo.objects.filter(pk=res).delete()
    return HttpResponseRedirect('/home')

@login_required
def statistics(request):
    c =[]
    m = []
    f = []
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    a = models.Employeeinfo.objects.filter(StaffNum=employ.EmployeeNum).all()
    for i in a:
        b = models.LeaveApplication.objects.filter(EmployeeNum=i.EmployeeNum).all()
        if b.count() != 0:
            c.append(b)
        h =0
    for x in c:
        h = h +1
        f.append(h)
        s = 0
        for y in x:
            s = y.Days+s
        m.append(s)
    d = a[0]
    context = {
        'ggg': 'active',
        'c': c,
        'f':f,
        'd': d,
        'm':m,
    }
    return render(request,'department/statistics.html',context)