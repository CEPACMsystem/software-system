# Generated by Django 3.1.2 on 2021-01-12 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserType', models.CharField(max_length=10, verbose_name='用户类型')),
                ('Name', models.CharField(max_length=11, verbose_name='姓名')),
                ('IdCard', models.CharField(max_length=20, verbose_name='身份证号')),
                ('Phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('UnitNumber', models.CharField(max_length=11, null=True, verbose_name='单元号')),
                ('FloorNumber', models.CharField(max_length=11, null=True, verbose_name='楼号')),
                ('HouseNumber', models.CharField(max_length=11, null=True, verbose_name='房间号')),
                ('Isolation', models.CharField(max_length=11, null=True, verbose_name='隔离标志')),
                ('Is', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.isolation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户注册',
                'verbose_name_plural': '用户注册',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datahelp', models.DateField(max_length=11, verbose_name='日期')),
                ('HelpType', models.CharField(max_length=11, verbose_name='帮助类型')),
                ('Details', models.CharField(max_length=100, verbose_name='详细介绍')),
                ('Appli', models.CharField(max_length=11, verbose_name='申请人')),
                ('Phone', models.CharField(max_length=100, verbose_name='手机号')),
                ('Place', models.CharField(max_length=100, verbose_name='住址')),
                ('ResPerson', models.CharField(max_length=11, null=True, verbose_name='负责人')),
                ('HelpSign', models.CharField(max_length=11, null=True, verbose_name='接受标志')),
                ('Helps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resident.userprofil')),
            ],
            options={
                'verbose_name': '互助申请',
                'verbose_name_plural': '互助申请',
            },
        ),
        migrations.CreateModel(
            name='GetOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataApply', models.DateField(max_length=11, verbose_name='申请日期')),
                ('Destination', models.CharField(max_length=11, verbose_name='目的地')),
                ('OutReason', models.CharField(max_length=11, verbose_name='原因')),
                ('OutSign', models.CharField(max_length=11, null=True, verbose_name='审核结果')),
                ('GOut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resident.userprofil')),
            ],
            options={
                'verbose_name': '出社区申请',
                'verbose_name_plural': '出社区申请',
            },
        ),
        migrations.CreateModel(
            name='GetInto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataInto', models.DateField(max_length=11, verbose_name='日期')),
                ('MainDes', models.CharField(max_length=11, verbose_name='停留地点')),
                ('Travel', models.CharField(max_length=11, verbose_name='重点地区')),
                ('Places', models.CharField(max_length=100, verbose_name='途径地')),
                ('IntoSign', models.CharField(max_length=11, null=True, verbose_name='审核结果')),
                ('Gin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resident.userprofil')),
            ],
            options={
                'verbose_name': '进社区申请',
                'verbose_name_plural': '进社区申请',
            },
        ),
        migrations.CreateModel(
            name='DailyUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datahelp', models.DateField(max_length=11, verbose_name='日期')),
                ('UseType', models.CharField(max_length=100, verbose_name='用品名称')),
                ('UseSign', models.CharField(max_length=11, null=True, verbose_name='查看标志')),
                ('Auditor', models.CharField(max_length=11, null=True, verbose_name='审核人')),
                ('Appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resident.userprofil')),
            ],
            options={
                'verbose_name': '用品申请',
                'verbose_name_plural': '用品申请',
            },
        ),
        migrations.CreateModel(
            name='DailyRepords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataReport', models.DateField(max_length=11, verbose_name='填报日期')),
                ('Temperature', models.FloatField(max_length=11, verbose_name='体温')),
                ('Isolated', models.CharField(max_length=11, verbose_name='是否隔离')),
                ('Cough', models.CharField(max_length=11, verbose_name='咳嗽')),
                ('Other', models.CharField(max_length=100, verbose_name='其他')),
                ('DayRepord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resident.userprofil')),
            ],
            options={
                'verbose_name': '每日上报',
                'verbose_name_plural': '每日上报',
            },
        ),
    ]
