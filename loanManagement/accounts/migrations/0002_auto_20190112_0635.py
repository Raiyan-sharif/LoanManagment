# Generated by Django 2.1 on 2019-01-12 06:35

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='users',
        ),
    ]
