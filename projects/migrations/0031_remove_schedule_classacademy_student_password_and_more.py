# Generated by Django 4.2.4 on 2023-09-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_schedule_classacademy_schedule_classroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='classAcademy',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contraseña'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contraseña'),
        ),
    ]
