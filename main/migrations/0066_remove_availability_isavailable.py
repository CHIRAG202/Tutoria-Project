# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0065_auto_20171118_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='isAvailable',
        ),
    ]
