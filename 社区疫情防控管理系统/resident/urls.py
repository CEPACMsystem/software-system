from django.conf.urls import url
from resident import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^mydailyrepord/', views.mydailyrepord, name='mydailyrepord'),
    url(r'^personalinfo/', views.personalinfo, name='personalinfo'),
]