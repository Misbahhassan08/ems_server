# Generated by Django 4.2.15 on 2024-09-06 13:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ems_app", "0033_alter_user_up_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="hardware_id",
        ),
    ]
