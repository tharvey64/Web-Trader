# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20150404_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='type_of',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
