# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150701_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 56, 35, 3856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 56, 35, 13957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 56, 34, 999120, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 56, 35, 1037, tzinfo=utc)),
        ),
    ]
