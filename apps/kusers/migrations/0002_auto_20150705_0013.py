# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='rol',
        ),
        migrations.AddField(
            model_name='basicuser',
            name='photo',
            field=models.ImageField(upload_to=b'/users/photo', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='cargo',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='departamento',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to=b'/users/photo', blank=True),
        ),
    ]
