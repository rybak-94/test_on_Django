# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20170214_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_1',
            field=models.IntegerField(blank=True, choices=[(2, 'Я счастливый человек'), (3, 'Я несчастен'), (1, 'Я смелый человек')], verbose_name='1 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_2',
            field=models.IntegerField(blank=True, choices=[(2, 'Я счастливый человек'), (3, 'Я несчастен'), (1, 'Я успешный человек')], verbose_name='2 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_3',
            field=models.IntegerField(blank=True, choices=[(3, 'Я не вижу'), (2, 'Я счастливый человек'), (1, 'Я хорошо вижу')], verbose_name='3 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.IntegerField(choices=[(3, 'Тест на зоркость'), (2, 'Тест на успешность'), (1, 'Тест на смелось')], verbose_name='Название вопроса'),
        ),
    ]