# Generated by Django 2.0.4 on 2018-05-13 12:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPI', '0005_auto_20180513_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 13, 12, 6, 57, 762269, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 13, 12, 6, 57, 762349, tzinfo=utc)),
        ),
    ]
