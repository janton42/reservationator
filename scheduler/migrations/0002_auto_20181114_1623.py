# Generated by Django 2.1.3 on 2018-11-15 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinstance',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]
