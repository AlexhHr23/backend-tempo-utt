# Generated by Django 4.0.2 on 2023-08-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_classroom_building'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classrooms_assigned',
            field=models.ManyToManyField(to='projects.Classroom'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects_taught',
            field=models.ManyToManyField(to='projects.Subject'),
        ),
    ]