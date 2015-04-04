# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('users', '0002_auto_20150403_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerageAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='BrokerageClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='brokerageaccount',
            name='client',
            field=models.ForeignKey(to='brokerage.BrokerageClient'),
        ),
    ]
