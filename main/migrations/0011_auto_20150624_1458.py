# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150623_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 11, 58, 46, 125911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 11, 58, 46, 128121, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 11, 58, 46, 124368, tzinfo=utc)),
        ),
    ]
