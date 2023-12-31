# Generated by Django 3.0 on 2023-11-09 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20231109_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
