# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint1', '0002_auto_20170911_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=254, null=True)),
                ('latitude', models.IntegerField(null=True)),
                ('longtiude', models.IntegerField(null=True)),
            ],
        ),
    ]