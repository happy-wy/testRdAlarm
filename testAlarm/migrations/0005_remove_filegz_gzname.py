# Generated by Django 2.0 on 2019-01-02 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testAlarm', '0004_filegz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filegz',
            name='GzName',
        ),
    ]
