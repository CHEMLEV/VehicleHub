# Generated by Django 4.2 on 2023-06-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0030_remove_vehicle_make_vehicle_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemake',
            name='logo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
