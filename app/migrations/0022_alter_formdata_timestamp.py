# Generated by Django 4.2.14 on 2025-01-12 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_formdata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='timestamp',
            field=models.DateField(default=datetime.date(2025, 1, 12)),
        ),
    ]
