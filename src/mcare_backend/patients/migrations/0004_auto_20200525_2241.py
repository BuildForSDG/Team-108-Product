# Generated by Django 2.2.12 on 2020-05-25 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20200525_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprofile',
            name='assigned_class',
        ),
        migrations.AddField(
            model_name='expertclass',
            name='members',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.PatientProfile'),
        ),
    ]
