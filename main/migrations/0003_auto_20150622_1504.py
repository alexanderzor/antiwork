# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150622_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to=b'images/', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 12, 4, 36, 796123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 12, 4, 36, 794302, tzinfo=utc)),
        ),
    ]
