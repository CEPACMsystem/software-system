from django.shortcuts import render

# Create your views here.

def manage(request):
    return render(request,'administrator/ad_base.html')


def ad_getout(request):
    return render(request, 'administrator/ad_getout.html')