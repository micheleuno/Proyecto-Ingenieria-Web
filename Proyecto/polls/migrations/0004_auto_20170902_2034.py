# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Supervisor')], default=1),
        ),
    ]
