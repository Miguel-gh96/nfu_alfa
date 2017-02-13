# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default=b'', max_length=100)),
                ('email', models.CharField(blank=True, default=b'', max_length=100)),
                ('to', models.CharField(blank=True, default=b'', max_length=100)),
                ('subject', models.CharField(blank=True, default=b'', max_length=100)),
                ('message', models.CharField(blank=True, default=b'', max_length=500)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]