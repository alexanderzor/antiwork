# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20150701_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 53, 23, 604081, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='feedbackcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 53, 23, 607866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 53, 23, 599509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 53, 23, 601476, tzinfo=utc)),
        ),
    ]
