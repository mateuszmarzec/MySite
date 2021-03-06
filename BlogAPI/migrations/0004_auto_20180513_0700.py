# Generated by Django 2.0.4 on 2018-05-13 07:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPI', '0003_auto_20180513_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 13, 7, 0, 15, 766520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 13, 7, 0, 15, 766432, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
