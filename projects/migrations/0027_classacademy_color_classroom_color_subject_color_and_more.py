# Generated by Django 4.2.4 on 2023-09-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_rename_teachers_schedule_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classacademy',
            name='color',
            field=models.CharField(default='FFFFFFF', max_length=7, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='color',
            field=models.CharField(default='FFFFFFF', max_length=7, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='subject',
            name='color',
            field=models.CharField(default='FFFFFFF', max_length=7, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='color',
            field=models.CharField(default='FFFFFFF', max_length=7, verbose_name='Color'),
        ),
    ]
