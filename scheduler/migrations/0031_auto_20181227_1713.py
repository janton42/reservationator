# Generated by Django 2.1.3 on 2018-12-28 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0030_auto_20181227_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='event',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]
