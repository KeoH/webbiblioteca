# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('kusers', '0005_auto_20150712_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kuser',
            options={'verbose_name': 'Usuario KSap', 'verbose_name_plural': 'Usuarios KSap'},
        ),
        migrations.AlterField(
            model_name='kuser',
            name='user',
            field=models.OneToOneField(verbose_name='Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
