# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='unpublish',
            field=models.BooleanField(default=False, verbose_name='Do not publish'),
        ),
    ]
