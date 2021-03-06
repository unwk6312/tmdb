# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0006_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=2000)),
                ('movie_review', models.CharField(default='None', max_length=2000)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmdb.movie_id')),
            ],
        ),
    ]
