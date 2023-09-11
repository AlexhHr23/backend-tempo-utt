# Generated by Django 4.0.2 on 2023-09-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_remove_classacademy_groups_classacademy_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classrooms_assigned',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classroom_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.classroom'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='class_academy',
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_academy',
            field=models.ManyToManyField(to='projects.ClassAcademy'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='Número telefónico'),
        ),
    ]