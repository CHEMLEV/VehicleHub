# Generated by Django 4.2 on 2023-06-21 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleHub', '0032_alter_customsrecord_country_of_origin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsrecord',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customsrecord',
            name='vehicle_id',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='VehicleHub.vehicle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='numberplate',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='numberplate',
            name='vehicle_id',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='VehicleHub.vehicle'),
            preserve_default=False,
        ),
    ]