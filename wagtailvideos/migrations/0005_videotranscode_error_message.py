# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailvideos', '0004_auto_20160706_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotranscode',
            name='error_message',
            field=models.TextField(blank=True),
        ),
    ]
