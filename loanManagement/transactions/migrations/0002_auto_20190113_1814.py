# Generated by Django 2.1 on 2019-01-13 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diposit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Diposit',
        ),
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.DeleteModel(
            name='Withdrawal',
        ),
    ]
