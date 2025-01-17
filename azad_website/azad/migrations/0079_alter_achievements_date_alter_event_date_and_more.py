# Generated by Django 4.1.4 on 2024-11-06 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0078_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 6, 22, 47, 11, 134058)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 22, 47, 11, 132057)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 22, 47, 11, 133038)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 6, 22, 47, 11, 134058)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 22, 47, 11, 132057)),
        ),
    ]
