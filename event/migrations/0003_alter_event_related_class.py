# Generated by Django 4.2.3 on 2024-03-30 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('event', '0002_remove_event_creator_event_related_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='related_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class'),
        ),
    ]
