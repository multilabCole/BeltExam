# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LogReg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('travel_datefrom', models.DateField()),
                ('travel_dateto', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('joined', models.ManyToManyField(related_name='Trips_joined', to='LogReg.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='LogReg.User')),
            ],
        ),
    ]