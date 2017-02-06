# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170206_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
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
            field=models.IntegerField(choices=[(3, 'Я не вижу'), (1, 'Я хорошо вижу'), (2, 'Я счастливый человек')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'User')]),
        ),
    ]
