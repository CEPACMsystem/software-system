from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns={
    #re_path(r'articles/2003/$',views.article_2003),
    re_path(r'article/(?P<arg1>[0-9]{4})/(?P<arg2>[0-9]{2})/(?P<slug>[\w-]+)/$',views.article_archive3)
    #re_path(r'article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.article_archive),
    # path('admin/',admin.site.urls),
    # path('test',views.test_view)
    # path('login',views.login_view)
}