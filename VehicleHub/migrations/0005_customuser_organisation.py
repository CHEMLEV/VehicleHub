# Generated by Django 4.2 on 2023-06-02 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0004_remove_customuser_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VehicleHub.organisation'),
        ),
    ]