# Generated by Django 4.2.4 on 2023-09-13 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_remove_group_career'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classacademy',
            name='groups',
        ),
    ]
