# Generated by Django 4.2.15 on 2024-09-05 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ems_app", "0015_hardware"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_Project",
            fields=[
                ("up_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ems_app.project",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ems_app.user"
                    ),
                ),
            ],
        ),
    ]
