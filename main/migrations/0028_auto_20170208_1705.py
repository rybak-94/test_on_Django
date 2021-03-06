# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20170208_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_1',
            field=models.IntegerField(blank=True, choices=[(3, 'Я несчастен'), (2, 'Я счастливый человек'), (1, 'Я смелый человек')], verbose_name='1 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_2',
            field=models.IntegerField(blank=True, choices=[(1, 'Я успешный человек'), (3, 'Я несчастен'), (2, 'Я счастливый человек')], verbose_name='2 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_3',
            field=models.IntegerField(blank=True, choices=[(2, 'Я счастливый человек'), (3, 'Я не вижу'), (1, 'Я хорошо вижу')], verbose_name='3 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.IntegerField(blank=True, choices=[(3, 'Тест на зоркость'), (2, 'Тест на успешность'), (1, 'Тест на смелось')], null=True),
        ),
        migrations.RemoveField(
            model_name='test',
            name='question_title',
        ),
        migrations.AddField(
            model_name='test',
            name='question_title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
    ]
