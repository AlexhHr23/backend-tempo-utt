# Generated by Django 4.0.2 on 2023-09-04 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_remove_teacher_classrooms_assigned_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
