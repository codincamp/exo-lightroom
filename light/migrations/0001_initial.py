# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('FF0000', 'Rouge'), ('00FF00', 'Vert'), ('0000FF', 'Bleu')], max_length=6)),
                ('state', models.IntegerField(choices=[(0, 'ON'), (1, 'OFF')], max_length=1)),
            ],
        ),
    ]
