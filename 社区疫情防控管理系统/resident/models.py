from django.db import models
from django.contrib.auth.models import User
from administrator import models1

# Create your models here.
class UserProfil(models.Model):
    UserType = models.CharField(verbose_name='用户类型',max_length=10)
    Name = models.CharField(verbose_name='姓名', max_length=11)
    IdCard = models.CharField(verbose_name='身份证号', max_length=20)
    Phone = models.CharField(verbose_name='手机号',max_length=11)
    UnitNumber = models.CharField(verbose_name='单元号',null=True,max_length=11)
    FloorNumber = models.CharField(verbose_name='楼号',null=True,max_length=11)
    HouseNumber = models.CharField(verbose_name='房间号',null=True,max_length=11)

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '用户注册'#对表设置

class DailyRepords(models.Model):
    DataReport = models.DateField(verbose_name='填报日期',max_length=11)
    Temperature = models.FloatField(verbose_name='体温',max_length=11)
    Isolated = models.CharField(verbose_name='是否隔离',max_length=11)
    Cough = models.CharField(verbose_name='咳嗽',max_length=11)
    Other = models.CharField(verbose_name='其他', max_length=100)
    DayRepord = models.ForeignKey(UserProfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.Temperature
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '每日上报'#对表设置

#出社区申请表
class GetOut(models.Model):
    DataApply = models.DateField(verbose_name='申请日期',max_length=11)
    Destination = models.CharField(verbose_name='目的地',max_length=11)
    OutReason = models.CharField(verbose_name='原因',max_length=11)
    GOut= models.ForeignKey(UserProfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.Destination
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '出社区申请'#对表设置

#进社区申请表
class GetInto(models.Model):
    DataInto = models.DateField(verbose_name='日期',max_length=11)
    MainDes = models.CharField(verbose_name='停留地点',max_length=11)
    Travel = models.CharField(verbose_name='重点地区',max_length=11)
    Places = models.CharField(verbose_name='途径地', max_length=100)
    Gin = models.ForeignKey(UserProfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.MainDes
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '进社区申请'#对表设置

#互助申请表
class Help(models.Model):
    Datahelp = models.DateField(verbose_name='日期',max_length=11)
    HelpType = models.CharField(verbose_name='帮助类型',max_length=11)
    Details = models.CharField(verbose_name='详细介绍',max_length=100)
    ResPerson = models.CharField(verbose_name='负责人',max_length=11,null=True)
    HelpSign = models.CharField(verbose_name='接受标志',max_length=11,null=True)
    # Places = models.CharField(verbose_name='途径地', max_length=100)
    Helps = models.ForeignKey(UserProfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.HelpType
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '互助申请'#对表设置

#用品申请
class DailyUse(models.Model):
    Datahelp = models.DateField(verbose_name='日期',max_length=11)
    UseType = models.CharField(verbose_name='用品名称',max_length=100)
    UseSign = models.CharField(verbose_name='查看标志',max_length=11,null=True)
    Auditor = models.CharField(verbose_name='审核人',max_length=11,null=True)
    # Places = models.CharField(verbose_name='途径地', max_length=100)
    Appliance = models.ForeignKey(UserProfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.Datahelp
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '用品申请'#对表设置