# Generated by Django 4.2 on 2023-06-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0034_alter_ownership_user_id_alter_ownership_vehicle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownership',
            old_name='vehicle',
            new_name='vehicle_id',
        ),
    ]
