# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type_of',
            field=models.CharField(default=datetime.datetime(2015, 4, 4, 20, 59, 31, 475089, tzinfo=utc), max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
