# Generated by Django 4.2 on 2023-06-28 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0040_alter_maintenancerecord_products_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breachtype',
            name='breach_type_title',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='punishmenttype',
            name='punishment_type_title',
            field=models.TextField(max_length=100),
        ),
    ]