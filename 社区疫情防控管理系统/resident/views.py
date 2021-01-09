from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from resident import models
import qrcode
from six import BytesIO
from administrator import models1
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
                    print(users)
                    print(c)
                    if c == types.UserType and types.UserType == '小区居民':
                        print(c)
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
        return HttpResponseRedirect('/resident')
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
        return HttpResponseRedirect('/resident')
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