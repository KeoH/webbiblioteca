# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kusers', '0002_auto_20150705_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to=b'users/photo', blank=True),
        ),
        migrations.DeleteModel(
            name='BasicUser',
        ),
    ]
