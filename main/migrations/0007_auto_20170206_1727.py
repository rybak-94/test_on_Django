# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170206_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='question_1',
        ),
        migrations.RemoveField(
            model_name='test',
            name='question_2',
        ),
        migrations.RemoveField(
            model_name='test',
            name='question_3',
        ),
    ]
