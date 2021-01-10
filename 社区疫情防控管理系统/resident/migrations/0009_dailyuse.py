# Generated by Django 3.1.2 on 2021-01-10 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0008_auto_20210110_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datahelp', models.DateField(max_length=11, verbose_name='日期')),
                ('UseType', models.CharField(max_length=11, verbose_name='用品名称')),
                ('UseSign', models.CharField(max_length=100, null=True, verbose_name='查看标志')),
                ('Auditor', models.CharField(max_length=11, null=True, verbose_name='审核人')),
                ('Appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resident.userprofil')),
            ],
            options={
                'verbose_name': '用品申请',
                'verbose_name_plural': '用品申请',
            },
        ),
    ]
