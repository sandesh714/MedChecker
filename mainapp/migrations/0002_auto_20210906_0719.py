# Generated by Django 2.2.20 on 2021-09-06 07:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='Date_From',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='Date_To',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='weeks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=56),
        ),
    ]
