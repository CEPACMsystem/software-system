# Generated by Django 3.1.2 on 2021-01-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EpidemicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InfoName', models.CharField(max_length=100, verbose_name='信息名称')),
                ('InfoLink', models.CharField(max_length=100, verbose_name='信息链接')),
                ('InfoDate', models.CharField(max_length=20, verbose_name='信息时间')),
            ],
            options={
                'verbose_name': '疫情信息',
                'verbose_name_plural': '疫情信息',
            },
        ),
        migrations.CreateModel(
            name='Isolation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=11, verbose_name='姓名')),
                ('IsolationSign', models.CharField(max_length=11, verbose_name='隔离标志')),
            ],
            options={
                'verbose_name': '隔离信息',
                'verbose_name_plural': '隔离信息',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=11, verbose_name='物品名称')),
                ('Acount', models.FloatField(max_length=11, verbose_name='数量')),
            ],
            options={
                'verbose_name': '物品名称',
                'verbose_name_plural': '物品名称',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PolicyName', models.CharField(max_length=100, verbose_name='政策名称')),
                ('PolicyLink', models.CharField(max_length=100, verbose_name='政策链接')),
                ('PolicyDate', models.CharField(max_length=20, verbose_name='政策时间')),
            ],
            options={
                'verbose_name': '疫情政策',
                'verbose_name_plural': '疫情政策',
            },
        ),
    ]
