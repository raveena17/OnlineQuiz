# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-01 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aptitude', '0004_question_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='A',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='B',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='C',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='D',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
