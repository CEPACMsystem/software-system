from django.conf.urls import url
from Employee import views

urlpatterns = [
    url(r'^$', views.employee1, name='employee1'),
    url(r'^fanhui/', views.fanhui, name='fanhui'),
    url(r'^application_add/', views.application_add, name='application_add'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^search/', views.search, name='search'),
    url(r'^manage/', views.manage, name='manage'),
    url(r'^myhistoappli/', views.myhistoappli, name='myhistoappli'),
]
