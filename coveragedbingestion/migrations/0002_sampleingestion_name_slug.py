# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-27 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coveragedbingestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampleingestion',
            name='name_slug',
            field=models.SlugField(editable=False, max_length=200, null=True, unique=True),
        ),
    ]
