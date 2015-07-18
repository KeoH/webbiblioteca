# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kusers', '0006_auto_20150712_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kuser',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
