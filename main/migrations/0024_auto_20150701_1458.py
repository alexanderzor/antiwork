# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20150701_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 58, 26, 603894, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 58, 26, 606865, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 58, 26, 599949, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 11, 58, 26, 601527, tzinfo=utc)),
        ),
    ]
