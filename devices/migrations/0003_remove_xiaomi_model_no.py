# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20171003_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xiaomi',
            name='model_no',
        ),
    ]
