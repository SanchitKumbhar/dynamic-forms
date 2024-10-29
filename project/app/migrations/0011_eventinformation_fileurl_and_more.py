# Generated by Django 4.2.14 on 2024-08-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_about_eventinformation_eventabout_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinformation',
            name='fileurl',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='eventinformation',
            name='eventfile',
            field=models.FileField(upload_to='files/'),
        ),
    ]
