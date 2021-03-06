# Generated by Django 2.1.3 on 2018-11-17 20:43

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20181114_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinstance',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='place',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2),
        ),
    ]
