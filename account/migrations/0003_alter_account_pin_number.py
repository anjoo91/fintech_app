# Generated by Django 4.2.2 on 2023-09-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_pin_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin_number',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]
