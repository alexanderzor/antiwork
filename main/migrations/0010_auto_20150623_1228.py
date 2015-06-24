# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150622_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='content',
            new_name='content1',
        ),
        migrations.AddField(
            model_name='new',
            name='content2',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 9, 28, 44, 391977, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 9, 28, 44, 396279, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 9, 28, 44, 389157, tzinfo=utc)),
        ),
    ]
