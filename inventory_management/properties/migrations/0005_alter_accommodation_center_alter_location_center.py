# Generated by Django 5.1.3 on 2024-12-04 06:07

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_accommodation_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='center',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='location',
            name='center',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
