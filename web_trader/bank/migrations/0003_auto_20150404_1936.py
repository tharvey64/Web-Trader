# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150403_2218'),
        ('accounts', '0002_auto_20150404_1906'),
        ('bank', '0002_auto_20150404_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type_of', models.CharField(max_length=100)),
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BankClient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('user', models.ForeignKey(to='users.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='client',
            field=models.ForeignKey(to='bank.BankClient'),
            preserve_default=True,
        ),
    ]
