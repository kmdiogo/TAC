# Generated by Django 2.1.3 on 2018-11-09 17:05

import Dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0013_merge_20181108_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='date',
            field=models.DateField(validators=[Dashboard.models.validate_date]),
        ),
    ]