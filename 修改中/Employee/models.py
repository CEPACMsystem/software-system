from django.db import models
from django.contrib.auth.models import User
from department import models1
# Create your models here.
class Employeeinfo(models.Model):
    EmployeeNum = models.IntegerField(verbose_name= '员工编号')
    EmployeeName = models.CharField(verbose_name= '姓名',max_length=20)
    StaffNum = models.IntegerField(verbose_name= '领导编号')
    DepartmentNum = models.CharField(verbose_name= '部门',max_length=10)
    employ = models.OneToOneField('UserProfil', on_delete=models.CASCADE)
    mde = models.ForeignKey(models1.DepartMent, on_delete=models.CASCADE)
    def __str__(self):
        return self.EmployeeName
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '员工信息'#对表设置
class LeaveApplication(models.Model):
    Applidate = models.DateTimeField(verbose_name='日期')
    EmployeeNum = models.IntegerField(verbose_name='员工编号')
    AppliType = models.CharField(verbose_name= '请假类型',max_length=10)
    BeginTime = models.DateField(verbose_name= '开始日期')
    EndTime = models.DateField(verbose_name= '结束日期')
    Days = models.IntegerField(verbose_name= '累计天数')
    Reason = models.CharField(verbose_name= '请假原因',max_length=500)
    ConfirmLogo = models.CharField(verbose_name= '确认标志',max_length=5,null=True)
    ConfirmName = models.CharField(verbose_name= '确认人',max_length=20)
    Em = models.ForeignKey('UserProfil',on_delete=models.CASCADE)

    def __int__(self):
        return self.EmployeeNum
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '请假'#对表设置


#用户注册信息表
class UserProfil(models.Model):
    UserType = models.CharField(verbose_name='用户类型',max_length=10)
    Phone = models.CharField(verbose_name='手机号',max_length=11)
    nick = models.CharField(verbose_name='昵称',max_length=6)
    EmployeeNum = models.IntegerField(verbose_name='用户编号')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    departms = models.ForeignKey(models1.DepartMent,on_delete=models.CASCADE)

    def __str__(self):
        return self.nick
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '用户注册'#对表设置

