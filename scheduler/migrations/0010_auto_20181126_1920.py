# Generated by Django 2.1.3 on 2018-11-27 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20181117_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='eventinstance',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='eventinstance',
            name='time',
        ),
        migrations.AlterField(
            model_name='eventinstance',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='time and date'),
        ),
        migrations.AlterField(
            model_name='eventinstance',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]
