# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empdtls',
            name='id',
        ),
        migrations.AlterField(
            model_name='empdtls',
            name='emp_id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]
