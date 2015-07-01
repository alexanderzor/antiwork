# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20150701_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='company',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 48, 53, 305926, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 48, 53, 308722, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 48, 53, 301409, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 48, 53, 303262, tzinfo=utc)),
        ),
    ]
