# Generated by Django 2.2.1 on 2019-06-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_centers', '0007_diagnosticstaff_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosticadmin',
            name='admin',
            field=models.BooleanField(default=True),
        ),
    ]