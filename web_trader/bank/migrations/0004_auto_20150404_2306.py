# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20150404_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='type_of',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
    ]
