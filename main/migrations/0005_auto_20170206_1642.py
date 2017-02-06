# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170206_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='question_1',
            field=models.IntegerField(choices=[(1, 'Я смелый человек'), (2, 'Я счастливый человек'), (3, 'Я несчастен')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_2',
            field=models.IntegerField(choices=[(2, 'Я счастливый человек'), (3, 'Я несчастен'), (1, 'Я успешный человек')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_3',
            field=models.IntegerField(choices=[(2, 'Я счастливый человек'), (1, 'Я хорошо вижу'), (3, 'Я не вижу')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=200, default=0),
        ),
    ]
