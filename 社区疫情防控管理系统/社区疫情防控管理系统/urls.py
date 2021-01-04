"""社区疫情防控管理系统 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from resident import urls as resident_urls
from administrator import urls as administrator_urls
from resident import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^resident/',include(resident_urls),name = 'resident'),
    url(r'^administrator/', include(administrator_urls),name= 'administrator'),
    url(r'^reg/',views.reg,name='reg'),
]
