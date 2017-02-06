# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170206_1616'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Title_test',
        ),
        migrations.AddField(
            model_name='test',
            name='title',
            field=models.IntegerField(default=0, choices=[(2, 'Тест на успешность'), (3, 'Тест на зоркость'), (1, 'Тест на смелось')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_1',
            field=models.IntegerField(choices=[(2, 'Я счастливый человек'), (3, 'Я несчастен'), (1, 'Я смелый человек')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_2',
            field=models.IntegerField(choices=[(2, 'Я счастливый человек'), (3, 'Я несчастен'), (1, 'Я успешный человек')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_3',
            field=models.IntegerField(choices=[(2, 'Я счастливый человек'), (3, 'Я не вижу'), (1, 'Я хорошо вижу')]),
        ),
    ]
