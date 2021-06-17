# Generated by Django 3.2.3 on 2021-05-23 14:16
from django_datetime.date_time import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('priority', models.CharField(blank=True, choices=[('NORMAL', 'normal'), ('REGULAR', 'regular'), ('VIP', 'vip'), ('TOP', 'top')], max_length=60, null=True)),
                ('created_date', models.DateField(default=datetime.dnow())),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('country_code', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('national', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('national_number', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('international', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('international_standard', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('type', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_phones', to='customer_models.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('map', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to='customer_models.customer')),
            ],
        ),
    ]
