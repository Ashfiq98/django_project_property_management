# Generated by Django 5.1.3 on 2024-12-04 05:53

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_alter_location_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='center',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
