# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-02 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aptitude', '0006_auto_20170801_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('score_value', models.IntegerField(default=0)),
            ],
        ),
    ]
