from django.db import models
from django.contrib.auth.models import User
from administrator import models1

# Create your models here.
class UserProfil(models.Model):
    UserType = models.CharField(verbose_name='用户类型',max_length=10)
    Name = models.CharField(verbose_name='姓名', max_length=11)
    IdCard = models.CharField(verbose_name='身份证号', max_length=20)
    Phone = models.CharField(verbose_name='手机号',max_length=11)
    UnitNumber = models.IntegerField(verbose_name='单元号')
    FloorNumber = models.IntegerField(verbose_name='楼号')
    HouseNumber = models.IntegerField(verbose_name='房间号')

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.UserType
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '用户注册'#对表设置

class DailyRepords(models.Model):
    DataReport = models.DateField(verbose_name='填报日期')
    Temperature = models.IntegerField(verbose_name='体温')
    Isolated = models.IntegerField(verbose_name='是否隔离')
    Cough = models.IntegerField(verbose_name='咳嗽')
    Other = models.CharField(verbose_name='其他', max_length=100)
    DayRepord = models.OneToOneField(UserProfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.DataReport
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '每日上报'#对表设置