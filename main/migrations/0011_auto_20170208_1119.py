# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170208_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='type_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.User', verbose_name='Тип пользователя'),
        ),
    ]
