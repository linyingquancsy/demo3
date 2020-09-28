# Generated by Django 3.1.1 on 2020-09-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
