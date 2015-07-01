# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150701_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 54, 19, 345192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 54, 19, 355175, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 54, 19, 340572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 9, 54, 19, 342440, tzinfo=utc)),
        ),
    ]
