# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_tutor_tutor_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
        ),
        migrations.RenameModel(
            old_name='Courses',
            new_name='SearchTag',
        ),
        migrations.AlterModelOptions(
            name='searchtag',
            options={},
        ),
        migrations.RenameField(
            model_name='searchtag',
            old_name='name',
            new_name='tagName',
        ),
        migrations.AddField(
            model_name='availability',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='searchTags',
            field=models.ManyToManyField(to='main.SearchTag'),
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='courses',
        ),
        migrations.AlterUniqueTogether(
            name='availability',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='availability',
            name='day',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='month',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='weekday',
        ),
        migrations.AddField(
            model_name='tutor',
            name='courses',
            field=models.ManyToManyField(to='main.Course'),
        ),
    ]
