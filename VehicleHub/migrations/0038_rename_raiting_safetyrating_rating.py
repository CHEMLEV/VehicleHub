# Generated by Django 4.2 on 2023-06-27 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0037_vehicle_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='safetyrating',
            old_name='raiting',
            new_name='rating',
        ),
    ]