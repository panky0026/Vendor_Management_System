# Generated by Django 5.0.4 on 2024-05-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_vendor_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(),
        ),
    ]
