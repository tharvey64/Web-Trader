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
            name='BankAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('type_of', models.CharField(max_length=100)),
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='BankClient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='client',
            field=models.ForeignKey(to='bank.BankClient'),
        ),
    ]
