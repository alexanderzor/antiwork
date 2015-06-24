# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150624_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 54, 11, 574141, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 54, 11, 576348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='first_name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 54, 11, 572541, tzinfo=utc)),
        ),
    ]
