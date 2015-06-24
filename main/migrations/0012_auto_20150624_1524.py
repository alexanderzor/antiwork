# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150624_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 24, 27, 446324, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 24, 27, 448473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 24, 27, 444790, tzinfo=utc)),
        ),
    ]
