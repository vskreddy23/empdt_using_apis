# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-25 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20170325_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdtls',
            name='contact_no',
            field=models.IntegerField(),
        ),
    ]
