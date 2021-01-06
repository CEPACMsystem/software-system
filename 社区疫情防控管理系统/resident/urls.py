from django.conf.urls import url
from resident import views

urlpatterns = [
    url(r'^$', views.personalinfo,name='personalinfo'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^mydailyrepord/', views.mydailyrepord, name='mydailyrepord'),
    # url(r'^personalinfo/', views.personalinfo, name='personalinfo'),
    # url(r'^getout/', views.getout, name='getout'),
    url(r'^getinto/', views.getinto, name='getinto'),
    url(r'^scode/', views.scode, name='scode'),
]