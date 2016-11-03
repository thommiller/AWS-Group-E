# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-02 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=1024)),
                ('note', models.CharField(default='', max_length=65536)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('passwordHash', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='citation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citations.User'),
        ),
    ]
