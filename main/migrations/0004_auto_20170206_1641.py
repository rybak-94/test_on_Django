# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170206_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_1',
            field=models.IntegerField(choices=[(3, 'Я несчастен'), (1, 'Я смелый человек'), (2, 'Я счастливый человек')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_2',
            field=models.IntegerField(choices=[(3, 'Я несчастен'), (2, 'Я счастливый человек'), (1, 'Я успешный человек')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_3',
            field=models.IntegerField(choices=[(1, 'Я хорошо вижу'), (2, 'Я счастливый человек'), (3, 'Я не вижу')]),
        ),
    ]
