# Generated by Django 4.2 on 2023-06-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0021_remove_ownership_vehicle_id_ownership_vehicle'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FinanceRecord',
        ),
    ]