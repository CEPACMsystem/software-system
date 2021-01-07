from django.db import models
import datetime

# Create your models here.
class DepartMent(models.Model):
    DepartMentNum = models.IntegerField(verbose_name='部门编号')
    DepartMentName = models.CharField(verbose_name='部门名称', max_length=20)
    DepartMentSir = models.CharField(verbose_name='部门管理员',max_length=20)
    DepartMentStaffNum = models.IntegerField(verbose_name='管理员编号')

    def __str__(self):
        return self.DepartMentName
    class Meta:
        verbose_name = verbose_name_plural = '部门信息'#对表设置


