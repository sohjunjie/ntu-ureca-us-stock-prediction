# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmgr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ustwitternewsfeed',
            name='sentiment',
            field=models.DecimalField(decimal_places=12, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='ustwitternewsfeed',
            name='text2',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
