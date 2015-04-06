# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150404_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(max_digits=12, decimal_places=2, default=0),
            preserve_default=True,
        ),
    ]
