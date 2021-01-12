from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from resident import models
import qrcode
from six import BytesIO
from administrator import models1
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.auth import logout, authenticate  # 登录，推出，验证
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import datetime

# Create your views here.
@login_required
def index(request):
    content = {
        'aaa':'active',
    }
    return render(request, 'home/base.html',content)


#登录
def user_login(request):
    if request.method == 'POST':
        a = request.POST.get('username', None)
        b = request.POST.get('password', None)
        c = request.POST.get('posts', None)
        user = models.User.objects.get(username=a)
        types = models.UserProfil.objects.get(user_id=user.id)
        if a and b:
            users = authenticate(username=a, password=b)  #如果验证成功，返回用户实例
            if users is not None:
                if users.is_active:
                    if c == types.UserType and types.UserType == '小区居民':
                        auth.login(request,users)
                        return HttpResponseRedirect('/resident')
                    elif c == types.UserType and types.UserType == '物业管理员':
                        auth.login(request,users)
                        return HttpResponseRedirect('/administrator')
                else:
                    return render(request, 'home/login.html', {'errer': '账号已被冻结'})
            else:
                return render(request, 'home/login.html', {'errer': '用户名或密码错误'})
    else:
        return render(request, 'home/login.html')

# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        Name = request.POST.get('Name', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        myidcard = request.POST.get('myidcard', None)
        menunum = request.POST.get('menunum',None)
        phone = request.POST.get('phone', None)
        floor = request.POST.get('floor',None)
        house = request.POST.get('house',None)
        usertype = request.POST.get('usertype',None)
        if username and password1 and password2:
            if password1 == password2:
                u_count = User.objects.filter(username=username).count()
                if u_count == 0:  # 没有这个用户名
                    # 用户自带表
                    user_info = {
                        'username': username,
                        'password': make_password(password1),
                    }
                    user_info1 = User.objects.create(**user_info)
                    try:
                        n = models1.Isolation.objects.get(Name=Name)
                    except ObjectDoesNotExist:
                        n = None
                    if n == None:
                        s = 0
                        print(s)
                    if n:
                        if menunum == '' and floor == '' and house == '':
                            user_profil2 = {
                                'Name': Name,
                                'Phone': phone,
                                'IdCard': myidcard,
                                'UnitNumber': 'null',
                                'FloorNumber': 'null',
                                'HouseNumber': 'null',
                                'UserType': usertype,
                                'Isolation':n.IsolationSign,
                                'Is_id': n.id,
                                'user': user_info1,
                            }
                            models.UserProfil.objects.create(**user_profil2)
                        else:
                            user_profil = {
                                'Name': Name,
                                'Phone': phone,
                                'IdCard': myidcard,
                                'UnitNumber': menunum,
                                'FloorNumber': floor,
                                'HouseNumber': house,
                                'UserType': usertype,
                                'Isolation': n.IsolationSign,
                                'Is_id':n.id,
                                'user': user_info1,
                            }
                            models.UserProfil.objects.create(**user_profil)
                    else:
                        if menunum == '' and floor == '' and house == '':
                            user_profil2 = {
                                'Name': Name,
                                'Phone': phone,
                                'IdCard': myidcard,
                                'UnitNumber': 'null',
                                'FloorNumber': 'null',
                                'HouseNumber': 'null',
                                'UserType': usertype,
                                'user': user_info1,
                            }
                            models.UserProfil.objects.create(**user_profil2)
                        else:
                            user_profil = {
                                'Name': Name,
                                'Phone': phone,
                                'IdCard': myidcard,
                                'UnitNumber': menunum,
                                'FloorNumber': floor,
                                'HouseNumber': house,
                                'UserType': usertype,
                                'user': user_info1,
                            }
                            models.UserProfil.objects.create(**user_profil)
                    return HttpResponseRedirect('/user_login')
                else:  # 用户已存在
                    return render(request, 'home/reg.html', {'errer': '用户名已存在'})
            else:
                return render(request, 'home/reg.html', {'errer': '两次密码不一样，请重新输入'})
        # 对注册信息做校验
    else:
        # s = models1.DepartMent.objects.all()
        # context = {
        #     's': s,
        # }
        return render(request, 'home/reg.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login')

#每日上报
@login_required
def mydailyrepord(request):
    if request.method == 'POST':
        a = request.POST.get('daydate', None)
        b = request.POST.get('temperatures', None)
        c = request.POST.get('isolate', None)
        d = request.POST.get('cough', None)
        e = request.POST.get('others', None)
        f = request.POST.get('rename', None)
        g = models.UserProfil.objects.get(Name=f)
        h = g.id
        dayre = {
            'DataReport': a,
            'Temperature': b,
            'Isolated': c,
            'Cough': d,
            'Other': e,
            'DayRepord_id': h,
        }
        models.DailyRepords.objects.create(**dayre)
        return HttpResponseRedirect('/resident')
    else:
        time = datetime.datetime.now()
        user = User.objects.get(id = request.user.id)
        report = models.UserProfil.objects.get(user_id=user.id)
        context = {
            'ccc': 'active',
            'time': time,
            'report': report
        }
        return render(request, 'resident/everydayrepord.html',context)

#个人信息
@login_required
def personalinfo(request):
    user = User.objects.get(id=request.user.id)
    employ = models.UserProfil.objects.get(user_id=user.id)
    # dep = models.DailyRepords.objects.get(DayRepord=employ.id)
    context = {
        'aaa': 'active',
        'user': user,
        'employ': employ,
        # 'dep': dep,
    }
    return render(request, 'resident/personalinfo.html', context)


#出社区申请
@login_required
def getout(request):
    if request.method == 'POST':
        a = request.POST.get('outdate', None)
        b = request.POST.get('destination', None)
        c = request.POST.get('reasons', None)
        d = request.POST.get('myoutname', None)
        e = models.UserProfil.objects.get(Name=d)
        f = e.id
        dayout = {
            'DataApply': a,
            'Destination': b,
            'OutReason': c,
            'GOut_id': f,
        }
        models.GetOut.objects.create(**dayout)
        return HttpResponseRedirect('/resident/getout')
    else:
        times = datetime.datetime.now()
        user = User.objects.get(id = request.user.id)
        gout = models.UserProfil.objects.get(user_id=user.id)
        context = {
            'ddd': 'active',
            'times': times,
            'gout': gout
        }
        return render(request, 'resident/getout.html',context)


#进社区申请
@login_required
def getinto(request):
    if request.method == 'POST':
        a = request.POST.get('intodate', None)
        b = request.POST.get('inportravel', None)
        c = request.POST.get('experience', None)
        d = request.POST.get('mainstop', None)
        e = request.POST.get('myintoname', None)
        f = models.UserProfil.objects.get(Name=e)
        g = f.id
        dayinto = {
            'DataInto': a,
            'MainDes': d,
            'Travel': b,
            'Places': c,
            'Gin_id': g,
        }
        models.GetInto.objects.create(**dayinto)
        return HttpResponseRedirect('/resident/getinto')
    else:
        timess = datetime.datetime.now()
        user = User.objects.get(id = request.user.id)
        ginto = models.UserProfil.objects.get(user_id=user.id)
        context = {
            'eee': 'active',
            'timess': timess,
            'ginto': ginto
        }
        return render(request, 'resident/getinto.html',context)


#生成二维码
@login_required
def scode(request):
    timesss = datetime.datetime.now()
    user = User.objects.get(id=request.user.id)
    ginto = models.UserProfil.objects.get(user_id=user.id)
    # myinfo = models.DailyRepords.objects.get(DayRepord_id=ginto.id)
    name = ginto.Name
    type = ginto.UserType
    idcard = ginto.IdCard
    phone = ginto.Phone
    unit = ginto.UnitNumber
    floor = ginto.FloorNumber
    house = ginto.HouseNumber
    # tem = myinfo.Temperature
    # iso = myinfo.Isolated
    # cough = myinfo.Cough
    datass = {
        'name' : name,
         'type' : type,
         'idcard' : idcard,
         'phone' : phone,
         'unit' : unit,
         'floor' : floor,
         'house' : house,
         # 'tem' : tem,
         # 'iso' : iso,
         # 'cough' : cough,
    }
    img = qrcode.make(datass)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    return HttpResponse(image_stream,content_type="image/png")

#查询
def query(request):
    return render(request,'resident/query.html')


#进社区申请查询
@login_required
def intocomquery(request):
    pn = request.GET.get('pn', None)
    user = User.objects.get(id=request.user.id)
    ginto = models.UserProfil.objects.get(user_id=user.id)
    emnum = models.GetInto.objects.filter(Gin_id=ginto.id).all()
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
    context = {
        'sss': 'active',
        'emnum': emnum,
        'a':a,
        'num_pages':num_pages,
        'numbers':numbers,
        'pn':pn,
    }
    return render(request, 'resident/intocomquery.html', context)


#出社区申请
@login_required
def outcomquery(request):
    pn = request.GET.get('pn', None)
    user = User.objects.get(id=request.user.id)
    ginto = models.UserProfil.objects.get(user_id=user.id)
    emnum = models.GetOut.objects.filter(GOut_id=ginto.id).all()
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
    context = {
        'sss': 'active',
        'emnum': emnum,
        'a': a,
        'num_pages': num_pages,
        'numbers': numbers,
        'pn': pn,
    }
    return render(request, 'resident/outcomquery.html', context)

#求助
def help(request):
    if request.method == 'POST':
        a = request.POST.get('helpdate', None)
        b = request.POST.get('helptype', None)
        c = request.POST.get('helpname', None)
        d = request.POST.get('helpdetails',None)
        e = request.POST.get('phone',None)
        f = request.POST.get('place',None)
        g = models.UserProfil.objects.get(Name=c)
        print(f)
        h = g.id
        dayre = {
            'Datahelp': a,
            'HelpType': b,
            'Appli': c,
            'Details': d,
            'Phone': e,
            'Helps_id': h,
            'Place': f,
        }
        models.Help.objects.create(**dayre)
        return HttpResponseRedirect('/resident/help')
    else:
        time = datetime.datetime.now()
        user = User.objects.get(id = request.user.id)
        report = models.UserProfil.objects.get(user_id=user.id)
        context = {
            'ccc': 'active',
            'time': time,
            'report': report
        }
        return render(request, 'resident/help.html',context)

#求助查看
def helplook(request):
    pn = request.GET.get('pn',None)
    user = User.objects.get(id=request.user.id)
    ghelp = models.UserProfil.objects.get(user_id=user.id)
    emnum = models.Help.objects.all()
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
    context = {
        'sss': 'active',
        'ghelp':ghelp,
        'emnum': emnum,
        'a': a,
        'num_pages':num_pages,
        'numbers':numbers,
        'pn':pn,
    }
    return render(request, 'resident/helplook.html', context)

#接受
def peopleagree(request):
    a = '接受'
    user = User.objects.get(id=request.user.id)
    b = models.UserProfil.objects.get(user_id=user.id)
    res = request.GET.get('eid', None)
    models.Help.objects.filter(pk=res).update(HelpSign=a,ResPerson=b.Name)
    return HttpResponseRedirect('/resident/helplook')

#不接受
# def noagree(request):
#     a = '不接受'
#     user = User.objects.get(id=request.user.id)
#     b = models.UserProfil.objects.get(user_id=user.id)
#     res = request.GET.get('eid', None)
#     models.Help.objects.filter(pk=res).update(HelpSign=a,ResPerson=b.Name)
#     return HttpResponseRedirect('/resident/helplook')

#生活用品申请
def dailyuse(request):
    if request.method == 'POST':
        a = request.POST.get('helpdate', None)
        b = request.POST.get('usetype', None)
        c = request.POST.get('helpname', None)
        g = models.UserProfil.objects.get(Name=c)
        h = g.id
        dayre = {
            'Datahelp': a,
            'UseType': b,
            'Appliance_id': h,
        }
        models.DailyUse.objects.create(**dayre)
        return HttpResponseRedirect('/resident/dailyuse')
    else:
        time = datetime.datetime.now()
        user = User.objects.get(id = request.user.id)
        report = models.UserProfil.objects.get(user_id=user.id)
        context = {
            'ddd': 'active',
            'time': time,
            'report': report
        }
        return render(request, 'resident/dailyuse.html',context)

#疫情信息
def epiinfo(request):
    info = models1.EpidemicInfo.objects.all()
    content = {
        'info':info,
    }
    return render(request,'resident/epiinfo.html',content)

#疫情政策
def policyinfo(request):
    info = models1.Policy.objects.all()
    content = {
        'info':info,
    }
    return render(request,'resident/policyinfo.html',content)

#结果查看
def dailyuselook(request):
    pn = request.GET.get('pn', None)
    user = User.objects.get(id=request.user.id)
    report = models.UserProfil.objects.get(user_id=user.id)
    usea = models.DailyUse.objects.filter(Appliance_id=report.id).all()
    try:
        pn = int(pn)
    except:
        pn = 1
    #分页
    s = Paginator(usea,2)#a1查询结果集,a2每页显示条数
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
        'ddd': 'active',
        'report': report,
        'usea':usea,
        'a': a,
        'num_pages': num_pages,
        'numbers': numbers,
        'pn': pn,
    }
    return render(request, 'resident/dailyuselook.html', context)