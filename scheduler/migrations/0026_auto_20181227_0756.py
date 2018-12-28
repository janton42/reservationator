# Generated by Django 2.1.3 on 2018-12-27 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0025_auto_20181227_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='event',
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
