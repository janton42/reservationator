# Generated by Django 2.1.3 on 2018-12-01 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20181126_2042'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventInstance',
            new_name='Choice',
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Place'),
        ),
    ]