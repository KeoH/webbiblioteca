# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kusers', '0004_auto_20150705_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kuser',
            name='cargo',
            field=models.CharField(default=b'-', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='kuser',
            name='departamento',
            field=models.CharField(default=b'-', max_length=255, blank=True),
        ),
    ]
