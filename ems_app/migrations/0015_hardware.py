# Generated by Django 4.2.15 on 2024-09-05 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ems_app", "0014_delete_hardware"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hardware",
            fields=[
                ("hardware_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("serial_number", models.CharField(max_length=100)),
                ("is_connected", models.BooleanField(default=False)),
                ("connected_at", models.DateTimeField(auto_now_add=True)),
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
