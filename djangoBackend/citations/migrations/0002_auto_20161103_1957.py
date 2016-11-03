# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citation',
            name='note',
        ),
        migrations.AddField(
            model_name='citation',
            name='author',
            field=models.CharField(max_length=256, default='0000000'),
        ),
        migrations.AddField(
            model_name='citation',
            name='date_acc',
            field=models.DateField(default='1970-01-01'),
        ),
        migrations.AddField(
            model_name='citation',
            name='date_pub',
            field=models.DateField(default='1970-01-01'),
        ),
        migrations.AddField(
            model_name='citation',
            name='notes',
            field=models.CharField(max_length=65536, default='0000000'),
        ),
        migrations.AlterField(
            model_name='citation',
            name='link',
            field=models.CharField(max_length=1024, default='0000000'),
        ),
        migrations.AlterField(
            model_name='citation',
            name='title',
            field=models.CharField(max_length=256, default='0000000'),
        ),
    ]
