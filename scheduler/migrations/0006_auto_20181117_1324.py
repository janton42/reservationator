# Generated by Django 2.1.3 on 2018-11-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20181117_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinstance',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventinstance',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]
