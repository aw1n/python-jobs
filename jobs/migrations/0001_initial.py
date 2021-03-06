# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, default='', max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('about_the_company', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_person', models.CharField(max_length=255)),
                ('web_page', models.URLField(blank=True, default='', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to='jobs.Category')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to='cities_light.City')),
            ],
        ),
    ]
