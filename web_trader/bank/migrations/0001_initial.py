# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('accounts', '0001_initial'),
<<<<<<< HEAD
        ('users', '0001_initial'),
=======
>>>>>>> connor
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type_of', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
=======
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('type_of', models.CharField(max_length=100)),
>>>>>>> connor
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='BankClient',
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
        migrations.AddField(
            model_name='bankaccount',
            name='client',
            field=models.ForeignKey(to='bank.BankClient'),
        ),
    ]
