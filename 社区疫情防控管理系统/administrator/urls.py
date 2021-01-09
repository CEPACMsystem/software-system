from administrator import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.manage,name='manage'),
    url(r'^ad_getout/', views.ad_getout,name='ad_getout'),
]