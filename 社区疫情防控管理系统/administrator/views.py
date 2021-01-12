from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from resident import models
import qrcode
from six import BytesIO
from administrator import models1
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from resident import models
from django.contrib.auth import logout, authenticate  # 登录，推出，验证
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import datetime

# @login_required
# def manage(request):
#     return render(request,'administrator/adinfo.html')

#个人信息
@login_required
def adinfo(request):
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    # dep = models.DailyRepords.objects.get(DayRepord=employ.id)
    context = {
        'aaa': 'active',
        'user': user,
        'employ': employ,
        # 'dep': dep,
    }
    return render(request, 'administrator/adinfo.html', context)

#隔离人员信息
def isolation(request):
    return render(request,'administrator/isolation.html')

#添加隔离人员
def add_isolation(request):
    if request.method == 'POST':
        a = request.POST.get('name', None)
        b = request.POST.get('isolationtype', None)
        dayinto = {
            'Name': a,
            'IsolationSign':b,
        }
        models1.Isolation.objects.create(**dayinto)
        return HttpResponseRedirect('/administrator/isolation/add_isolation')
    else:
        context = {
            'eee': 'active',
        }
        return render(request, 'administrator/add_isolation.html',context)

#查看隔离人员
def look_isolation(request):
    pn = request.GET.get('pn', None)
    a = models1.Isolation.objects.all()
    b = models.UserProfil.objects.filter(Isolation = '隔离').all()
    try:
        pn = int(pn)
    except:
        pn = 1
    #分页
    s = Paginator(b,2)#a1查询结果集,a2每页显示条数
    try:
        a = s.page(pn) #获取某一页记录
    except (EmptyPage,InvalidPage,PageNotAnInteger) as e:
        pn =1
        a = s.page(pn)
    num_pages = a.paginator.num_pages
    if num_pages >= 5:  # 总页数大于你想要显示的分页数字
        if pn <= 2:
            start = 1
            end = 6
        elif pn > num_pages - 2:  # 10页  pn:9
            start = num_pages - 4
            end = num_pages + 1
        else:
            start = pn - 2
            end = pn + 3
    else:
        start = 1
        end = num_pages + 1

    numbers = range(start, end)
    context = {
        'isolation':b,
        'a': a,
        'num_pages': num_pages,
        'numbers': numbers,
        'pn': pn,
    }
    return render(request,'administrator/look_isolation.html',context)

#隔离区域
def isolationarea(request):
    a = models1.Isolation.objects.all()
    b = models.UserProfil.objects.filter(Isolation='隔离').all()
    context = {
        'isolation': b,
    }
    return render(request, 'administrator/isolationarea.html', context)

#出入申请审核
def intoout(request):
    return render(request,'administrator/intoout.html')

#出社区审核
def outaudit(request):
    user = User.objects.get(id=request.user.id)
    out = models.GetOut.objects.filter(OutSign=None).all()
    a = models.UserProfil.objects.all()
    context = {
        'sss': 'active',
        'out': out,
        'a': a,
    }
    return render(request, 'administrator/outaudit.html', context)

# #同意
def agree(request):
    a = '同意'
    # user = User.objects.get(id=request.user.id)
    # b = models.UserProfil.objects.get(user_id=user.id)
    res = request.GET.get('eid', None)
    # sid = request.GET.get('sid',None)
    # print(sid)
    models.GetOut.objects.filter(pk=res).update(OutSign=a)
    return HttpResponseRedirect('/administrator/intoout/outaudit')

# 不接受
def noagree(request):
    a = '不同意'
    # user = User.objects.get(id=request.user.id)
    # b = models.UserProfil.objects.get(user_id=user.id)
    res = request.GET.get('eid', None)
    models.GetOut.objects.filter(pk=res).update(OutSign=a)
    return HttpResponseRedirect('/administrator/intoout/outaudit')

#进社区审核
def intoaudit(request):
    user = User.objects.get(id=request.user.id)
    into = models.GetInto.objects.filter(IntoSign=None).all()
    a = models.UserProfil.objects.all()
    context = {
        'sss': 'active',
        'into': into,
        'a': a,
    }
    return render(request, 'administrator/intoaudit.html', context)

# #同意
def agree1(request):
    a = '同意'
    # user = User.objects.get(id=request.user.id)
    # b = models.UserProfil.objects.get(user_id=user.id)
    res = request.GET.get('eid', None)
    # sid = request.GET.get('sid',None)
    # print(sid)
    models.GetInto.objects.filter(pk=res).update(IntoSign=a)
    return HttpResponseRedirect('/administrator/intoout/intoaudit')

# 不接受
def noagree1(request):
    a = '不同意'
    # user = User.objects.get(id=request.user.id)
    # b = models.UserProfil.objects.get(user_id=user.id)
    res = request.GET.get('eid', None)
    models.GetInto.objects.filter(pk=res).update(IntoSign=a)
    return HttpResponseRedirect('/administrator/intoout/intoaudit')

#业主信息查看
def ownerinfo(request):
    pn = request.GET.get('pn', None)
    emnum = models.UserProfil.objects.filter(UserType='小区居民').all()
    try:
        pn = int(pn)
    except:
        pn = 1
    #分页
    s = Paginator(emnum,2)#a1查询结果集,a2每页显示条数
    try:
        a = s.page(pn) #获取某一页记录
    except (EmptyPage,InvalidPage,PageNotAnInteger) as e:
        pn =1
        a = s.page(pn)
    num_pages = a.paginator.num_pages
    if num_pages >= 5:  # 总页数大于你想要显示的分页数字
        if pn <= 2:
            start = 1
            end = 6
        elif pn > num_pages - 2:  # 10页  pn:9
            start = num_pages - 4
            end = num_pages + 1
        else:
            start = pn - 2
            end = pn + 3
    else:
        start = 1
        end = num_pages + 1

    numbers = range(start, end)
    content = {
        'owner':emnum,
        'a': a,
        'num_pages': num_pages,
        'numbers': numbers,
        'pn': pn,
    }
    return render(request,'administrator/ownerinfo.html',content)

#添加物品
def acquisition(request):
    if request.method == 'POST':
        a = request.POST.get('itemname', None)
        b = request.POST.get('acount', None)
        dayinto = {
            'Item': a,
            'Acount':b,
        }
        models1.Material.objects.create(**dayinto)
        return HttpResponseRedirect('/administrator/acquisition')
    else:
        context = {
            'eee': 'active',
        }
        return render(request, 'administrator/acquisition.html',context)

#物资查看
def inspection(request):
    pn = request.GET.get('pn', None)
    s = models1.Material.objects.all()
    try:
        pn = int(pn)
    except:
        pn = 1
    #分页
    s = Paginator(s,2)#a1查询结果集,a2每页显示条数
    try:
        a = s.page(pn) #获取某一页记录
    except (EmptyPage,InvalidPage,PageNotAnInteger) as e:
        pn =1
        a = s.page(pn)
    num_pages = a.paginator.num_pages
    if num_pages >= 5:  # 总页数大于你想要显示的分页数字
        if pn <= 2:
            start = 1
            end = 6
        elif pn > num_pages - 2:  # 10页  pn:9
            start = num_pages - 4
            end = num_pages + 1
        else:
            start = pn - 2
            end = pn + 3
    else:
        start = 1
        end = num_pages + 1

    numbers = range(start, end)
    context = {
        'ma':s,
        'ma': a,
        'num_pages': num_pages,
        'numbers': numbers,
        'pn': pn,
    }
    return render(request,'administrator/inspection.html',context)

#物资申请审核
def appreview(request):
    user = User.objects.get(id=request.user.id)
    ghelp = models.UserProfil.objects.get(user_id=user.id)
    emnum = models.DailyUse.objects.all()
    users = models.UserProfil.objects.all()
    context = {
        'sss': 'active',
        'ghelp': ghelp,
        'emnum': emnum,
        'users':users,
    }
    return render(request, 'administrator/appreview.html', context)

#已经查看
def review(request):
    a = '已查看'
    user = User.objects.get(id=request.user.id)
    b = models.UserProfil.objects.get(user_id=user.id)
    res = request.GET.get('eid', None)
    models.DailyUse.objects.filter(pk=res).update(UseSign=a,Auditor=b.Name)
    return HttpResponseRedirect('/administrator/appreview')

#疫情信息添加
def epidemic(request):
    if request.method == 'POST':
        a = request.POST.get('infoname', None)
        b = request.POST.get('infolink', None)
        c = request.POST.get('infotime',None)
        dayinto = {
            'InfoName': a,
            'InfoLink':b,
            'InfoDate':c,
        }
        models1.EpidemicInfo.objects.create(**dayinto)
        return HttpResponseRedirect('/administrator/epidemic')
    else:
        time = datetime.datetime.now()
        context = {
            'eee': 'active',
            'time':time,
        }
        return render(request, 'administrator/epidemic.html',context)

def policy(request):
    if request.method == 'POST':
        a = request.POST.get('policyname', None)
        b = request.POST.get('policylink', None)
        c = request.POST.get('policytime',None)
        dayinto = {
            'PolicyName': a,
            'PolicyLink':b,
            'PolicyDate':c,
        }
        models1.Policy.objects.create(**dayinto)
        return HttpResponseRedirect('/administrator/policy')
    else:
        time = datetime.datetime.now()
        context = {
            'eee': 'active',
            'time':time,
        }
        return render(request, 'administrator/policy.html',context)

#数据统计
def datasta(request):
    emnum = models.DailyRepords.objects.all()
    users = models.UserProfil.objects.all()
    context = {
        'sss': 'active',
        'emnum': emnum,
        'users': users,
    }
    return render(request, 'administrator/datasta.html', context)