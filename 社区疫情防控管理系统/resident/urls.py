from django.conf.urls import url
from django.urls import path
from resident import views

urlpatterns = [
    url(r'^$', views.personalinfo,name='personalinfo'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('mydailyrepord/', views.mydailyrepord, name='mydailyrepord'),
    path('personalinfo/', views.personalinfo, name='personalinfo'),
    path('getout/', views.getout, name='getout'),
    path('getinto/', views.getinto, name='getinto'),
    path('scode/', views.scode, name='scode'),
    path('query/', views.query, name='query'),
    path('query/intocomquery/',views.intocomquery,name='intocomquery'),
    path('query/outcomquery/',views.outcomquery,name='outcomquery'),
    path('help/',views.help,name='help'),
    path('helplook/',views.helplook,name='helplook'),
    # path('help/noagree/',views.noagree,name='noagree'),
    path('help/agree/',views.agree,name='agree'),
    path('dailyuse/',views.dailyuse,name='dailyuse'),
]