# Generated by Django 4.0.2 on 2023-08-30 04:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='number_days',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Numero de dias'),
        ),
    ]