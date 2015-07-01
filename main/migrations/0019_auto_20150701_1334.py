# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150701_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='message',
            new_name='description',
        ),
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(upload_to=b'images/', blank=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 33, 58, 715865, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 33, 58, 718885, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 33, 58, 704079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 10, 33, 58, 706050, tzinfo=utc)),
        ),
    ]
