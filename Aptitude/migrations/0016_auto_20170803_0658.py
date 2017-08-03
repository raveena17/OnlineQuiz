# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aptitude', '0015_remove_question_answer_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='answer_text',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
