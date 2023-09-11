# Generated by Django 4.0.2 on 2023-09-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_rename_teacher_schedule_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='teachers',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='number_days',
            field=models.IntegerField(verbose_name='Numero de dias'),
        ),
    ]