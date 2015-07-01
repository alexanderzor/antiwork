# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150624_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.datetime(2015, 7, 1, 9, 30, 56, 346558, tzinfo=utc))),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.datetime(2015, 7, 1, 9, 30, 56, 334809, tzinfo=utc))),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='feedback',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 30, 56, 337349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 30, 56, 332756, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='newscomment',
            name='parent',
            field=models.ForeignKey(to='main.New'),
        ),
        migrations.AddField(
            model_name='feedbackcomment',
            name='parent',
            field=models.ForeignKey(to='main.Feedback'),
        ),
    ]
