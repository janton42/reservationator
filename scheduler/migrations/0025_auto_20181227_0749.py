# Generated by Django 2.1.3 on 2018-12-27 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0024_auto_20181227_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]