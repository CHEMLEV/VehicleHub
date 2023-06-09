# Generated by Django 4.2 on 2023-06-22 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0033_alter_customsrecord_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VehicleHub.vehicle'),
        ),
    ]
