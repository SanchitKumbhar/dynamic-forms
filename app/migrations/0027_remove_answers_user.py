# Generated by Django 4.2.14 on 2025-01-12 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_answers_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='user',
        ),
    ]
