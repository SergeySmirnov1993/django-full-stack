# Generated by Django 4.2.9 on 2024-02-14 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 18, 1, 21, 833640, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 18, 1, 21, 832991, tzinfo=datetime.timezone.utc)),
        ),
    ]