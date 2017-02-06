# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.IntegerField(verbose_name='auth.User')),
                ('question_1', models.IntegerField(choices=[(3, ''), (2, ''), (1, '')])),
                ('question_2', models.IntegerField(choices=[(3, ''), (2, ''), (1, '')])),
                ('question_3', models.IntegerField(choices=[(3, ''), (2, ''), (1, '')])),
            ],
        ),
        migrations.CreateModel(
            name='Title_test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.IntegerField(choices=[(1, 'Тест на смелось'), (3, 'Тест на зоркость'), (2, 'Тест на успешность')])),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.IntegerField(choices=[(2, 'User'), (1, 'Admin')]),
        ),
    ]
