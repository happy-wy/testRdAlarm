# Generated by Django 2.0 on 2018-12-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devid', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('time', models.BigIntegerField()),
                ('speed', models.FloatField()),
                ('picture', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('Aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testAlarm.DevID', to_field='devid')),
            ],
        ),
    ]
