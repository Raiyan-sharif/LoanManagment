# Generated by Django 2.2.7 on 2019-12-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_userprofile_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(default='', max_length=150, unique=True)),
                ('full_name', models.CharField(default='', max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.IntegerField(null=True, unique=True)),
                ('Address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('nationality', models.CharField(max_length=256)),
                ('occupation', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(default='', max_length=20, unique=True, verbose_name='account number')),
                ('account_holder_name', models.CharField(default='', max_length=150, verbose_name='username')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Male', max_length=1)),
                ('address', models.CharField(max_length=512)),
                ('contact_no', models.IntegerField(null=True, unique=True)),
                ('loan_ammount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('loan_period', models.IntegerField()),
                ('balance', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]