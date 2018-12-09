# Generated by Django 2.1.3 on 2018-12-07 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20181206_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='price_quartile',
            new_name='pricequartile',
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]