# Generated by Django 5.0.3 on 2024-06-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScanBarApp', '0002_alter_barcode_sap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcode',
            name='sap',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
