# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='address',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
