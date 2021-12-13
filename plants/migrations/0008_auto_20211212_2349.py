# Generated by Django 3.1.13 on 2021-12-13 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_auto_20211212_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 13, 6, 49, 45, 156176, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
