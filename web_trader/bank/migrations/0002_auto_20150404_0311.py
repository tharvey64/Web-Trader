# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='account',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='client',
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
        migrations.RemoveField(
            model_name='bankclient',
            name='user',
        ),
        migrations.DeleteModel(
            name='BankClient',
        ),
    ]
