# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
