# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0101_auto_20171125_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='avatar',
            field=models.ImageField(default='images/default_avatar.jpg', upload_to='profile_pics'),
        ),
    ]
