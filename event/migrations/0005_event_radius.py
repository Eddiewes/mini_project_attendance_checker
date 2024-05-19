# Generated by Django 4.2.3 on 2024-05-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_location_event_geolocation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='radius',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Radius'),
            preserve_default=False,
        ),
    ]