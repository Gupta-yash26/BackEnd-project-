# Generated by Django 2.0.13 on 2023-08-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0002_auto_20230826_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelclass',
            name='Account_Number',
            field=models.BigIntegerField(),
        ),
    ]
