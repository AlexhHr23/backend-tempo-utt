# Generated by Django 4.2.4 on 2023-09-13 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_remove_schedule_classacademy_student_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.schedule'),
        ),
    ]
