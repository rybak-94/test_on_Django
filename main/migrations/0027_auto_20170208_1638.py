# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20170208_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_1',
            field=models.IntegerField(blank=True, choices=[(2, 'Я счастливый человек'), (1, 'Я смелый человек'), (3, 'Я несчастен')], verbose_name='1 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_2',
            field=models.IntegerField(blank=True, choices=[(1, 'Я успешный человек'), (2, 'Я счастливый человек'), (3, 'Я несчастен')], verbose_name='2 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_3',
            field=models.IntegerField(blank=True, choices=[(2, 'Я счастливый человек'), (1, 'Я хорошо вижу'), (3, 'Я не вижу')], verbose_name='3 Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.IntegerField(blank=True, choices=[(2, 'Тест на успешность'), (1, 'Тест на смелось'), (3, 'Тест на зоркость')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_title',
            field=models.ManyToManyField(choices=[(2, 'Тест на успешность'), (1, 'Тест на смелось'), (3, 'Тест на зоркость')], default=1, to='main.Question'),
        ),
    ]
