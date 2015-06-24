# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.datetime(2015, 6, 19, 9, 44, 44, 807008, tzinfo=utc))),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anonymous', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('message', models.TextField()),
                ('file', models.FileField(upload_to=b'files/', blank=True)),
                ('theme', models.IntegerField()),
                ('company', models.ForeignKey(to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 6, 19, 9, 44, 44, 801817, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(to='main.New'),
        ),
    ]
