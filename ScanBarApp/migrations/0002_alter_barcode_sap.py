# Generated by Django 5.0.3 on 2024-06-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScanBarApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcode',
            name='sap',
            field=models.CharField(max_length=8),
        ),
    ]
