# Generated by Django 4.2.2 on 2023-11-01 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_kyc_identity_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]
