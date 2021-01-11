from django.db import models
from django.contrib.auth.models import User
from administrator import models1

# Create your models here.
class Isolation(models.Model):
    Name = models.CharField(verbose_name='姓名', max_length=11)
    IsolationSign = models.CharField(verbose_name='隔离标志', max_length=11)

    def __str__(self):
        return self.Name
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '隔离信息'#对表设置

#物资种类数量表
class Material(models.Model):
    Item = models.CharField(verbose_name='物品名称', max_length=11)
    Acount = models.FloatField(verbose_name='数量', max_length=11)

    def __str__(self):
        return self.Item
    #内部类
    class Meta:
        verbose_name = verbose_name_plural = '物品名称'#对表设置