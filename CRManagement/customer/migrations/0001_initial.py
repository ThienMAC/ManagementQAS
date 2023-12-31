# Generated by Django 4.2.3 on 2023-08-23 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerCode', models.CharField(max_length=50)),
                ('customerName', models.CharField(max_length=200)),
                ('customerAddress', models.CharField(blank=True, max_length=2000)),
                ('customerHotline', models.CharField(blank=True, max_length=20)),
                ('isActive', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_Customer_2created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_Customer_2modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractCode', models.CharField(max_length=50)),
                ('contractName', models.CharField(max_length=200)),
                ('contractVersion', models.CharField(max_length=20)),
                ('contractType', models.CharField(max_length=200)),
                ('contractSize', models.FloatField()),
                ('contractFile', models.FileField(upload_to='')),
                ('contractStatus', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('contractCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contract_Customer_2_contracCustomer', to='customer.customer')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_Contract_2created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_Contract_2modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
