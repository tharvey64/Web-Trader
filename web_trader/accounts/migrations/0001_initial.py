# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('number', models.CharField(unique=True, default=None, max_length=17)),
                ('balance', models.DecimalField(default=0, decimal_places=3, max_digits=12)),
            ],
        ),
    ]
