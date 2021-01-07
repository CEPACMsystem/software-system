from django.contrib import admin

# Register your models here.
from Employee import models
# Register your models here.

admin.site.register(models.Employeeinfo)#注册数据模型到django admin 后台
admin.site.register(models.LeaveApplication)
admin.site.register(models.UserProfil)
