# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(default=None, max_length=17, unique=True),
        ),
    ]
