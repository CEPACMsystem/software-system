# Generated by Django 3.0.6 on 2020-05-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='maphone',
            field=models.IntegerField(verbose_name='手机号'),
        ),
    ]
