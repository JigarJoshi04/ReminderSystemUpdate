# Generated by Django 3.1.1 on 2020-09-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('client_type', models.CharField(max_length=100)),
                ('staff_id', models.IntegerField()),
                ('ca_name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('gst', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('income_tax_activate', models.BooleanField()),
                ('gst_tax_activate', models.BooleanField()),
                ('companies_activate', models.BooleanField()),
                ('accounting_activate', models.BooleanField()),
                ('other_service1', models.BooleanField()),
                ('other_service2', models.BooleanField()),
                ('other_service3', models.BooleanField()),
                ('other_service4', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(max_length=100)),
                ('date_of_deadline', models.DateField()),
                ('actual_date_on_which_reminder_is_to_be_sent', models.DateField()),
                ('recurrence_type', models.IntegerField()),
            ],
        ),
    ]
