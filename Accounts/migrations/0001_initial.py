# Generated by Django 3.0 on 2023-11-09 07:47

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('firstname', models.CharField(default='', max_length=40)),
                ('lastname', models.CharField(default='', max_length=40)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=Accounts.models.get_profile_image_filepath)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
