# Generated by Django 5.2 on 2025-05-10 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_passwordresetcode_expired_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expired_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 10, 11, 57, 46, 903873), editable=False),
        ),
    ]
