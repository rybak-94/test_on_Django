# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170207_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'User')]),
        ),
    ]
