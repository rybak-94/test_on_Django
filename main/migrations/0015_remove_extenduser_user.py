# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_extenduser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extenduser',
            name='user',
        ),
    ]