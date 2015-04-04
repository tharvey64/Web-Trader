# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerageAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='BrokerageClient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='brokerageaccount',
            name='client',
            field=models.ForeignKey(to='brokerage.BrokerageClient'),
        ),
    ]
