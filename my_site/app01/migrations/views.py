from django.shortcuts import render, HttpResponse

def article_2003(request):
    return HttpResponse('article 2003')

def article_archive(request,year,month):
    return HttpResponse("article 动态 %s-%s" % (year,month))

def article_archive2(request,arg1,arg2):
    return HttpResponse("article 动态 %s-%s" % (arg1,arg2))

def article_archive3(request,arg1,arg2,slug):
    return HttpResponse("article 动态 %s-%s %s" % (arg1,arg2,slug))

def test_view(request):
    print("test beginning", request)
    print(dir(request))
    return HttpResponse("<h1>test result</h1>")


def login_view(request):
    # html = """
    #     <form method="post">
    #
    #         <input type="text" name="username">
    #         <input type="password" name="password">
    #
    #         <input type="submit" value="登录">
    #     </form>
    # """
    # return HttpResponse(html)
    return render(request,'form.html')