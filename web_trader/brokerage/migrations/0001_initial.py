# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('stocks', '0001_initial'),
=======
>>>>>>> connor
        ('users', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerageAccount',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
=======
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
>>>>>>> connor
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='BrokerageClient',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
=======
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
>>>>>>> connor
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(max_digits=12, decimal_places=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(to='brokerage.BrokerageClient')),
                ('company', models.ForeignKey(to='stocks.Company')),
            ],
        ),
        migrations.AddField(
            model_name='brokerageaccount',
            name='client',
            field=models.ForeignKey(to='brokerage.BrokerageClient'),
        ),
    ]
