# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.IntegerField(blank=True, choices=[(3, 'Тест на зоркость'), (2, 'Тест на успешность'), (1, 'Тест на смелось')], null=True)),
                ('question_1', models.IntegerField(blank=True, choices=[(1, 'Я смелый человек'), (3, 'Я несчастен'), (2, 'Я счастливый человек')], verbose_name='1 Вопрос')),
                ('question_2', models.IntegerField(blank=True, choices=[(1, 'Я успешный человек'), (3, 'Я несчастен'), (2, 'Я счастливый человек')], verbose_name='2 Вопрос')),
                ('question_3', models.IntegerField(blank=True, choices=[(1, 'Я хорошо вижу'), (2, 'Я счастливый человек'), (3, 'Я не вижу')], verbose_name='3 Вопрос')),
            ],
        ),
    ]
