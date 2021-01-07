
from django.conf.urls import url
from department import views

urlpatterns = [
    url(r'^$',views.department1,name='department1'),
    url(r'^emappliinfo/',views.emappliinfo,name='emappliinfo'),
    url(r'^noagree/',views.noagree,name='noagree'),
    url(r'^agree/',views.agree,name='agree'),
    url(r'^historyappli/',views.historyappli,name='historyappli'),
    url(r'^employeeinfo/',views.employeeinfo,name= 'employeeinfo'),
    url(r'^employee_add/',views.employee_add,name= 'employee_add'),
    url(r'^employee_change/', views.employee_change, name='employee_change'),
    url(r'^employee_del/', views.employee_del, name='employee_del'),
    url(r'^statistics',views.statistics,name='statistics'),
    # url(r'^query_appli/',views.query_appli,name='query_appli'),
    # url(r'^generate_tables/',views.generate_tables,name='generate_tables'),
]