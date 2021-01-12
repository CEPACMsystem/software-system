from administrator import views
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    url(r'^$', views.adinfo,name='manage'),
    path('isolation/',views.isolation,name='isolation'),
    path('adinfo/',views.adinfo,name='adinfo'),
    path('isolation/add_isolation/',views.add_isolation,name='add_isolation'),
    path('isolation/look_isolation/',views.look_isolation,name='look_isolation'),
    path('isolationarea/',views.isolationarea,name='isolationarea'),
    path('intoout/',views.intoout,name='intoout'),
    path('intoout/outaudit/',views.outaudit,name='outaudit'),
    path('intoout/outaudit/agree',views.agree,name='agree'),
    path('intoout/outaudit/noagree',views.noagree,name='noagree'),
    path('intoout/intoaudit/', views.intoaudit, name='intoaudit'),
    path('intoout/intoaudit/agree1', views.agree1, name='agree1'),
    path('intoout/intoaudit/noagree1', views.noagree1, name='noagree1'),
    path('ownerinfo/',views.ownerinfo,name='ownerinfo'),
    path('acquisition/',views.acquisition,name='acquisition'),
    path('inspection/',views.inspection,name='inspection'),
    path('appreview/',views.appreview,name='appreview'),
    path('appreview/review',views.review,name='review'),
    path('epidemic/',views.epidemic,name='epidemic'),
    path('policy/',views.policy,name='policy'),
    path('datasta/',views.datasta,name='datasta'),
    # path('adinfo',views.adinfo,name='adinfo'),
    # path('adinfo',views.adinfo,name='adinfo'),
]