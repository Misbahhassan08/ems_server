# Generated by Django 4.2.15 on 2024-09-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ems_app", "0029_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="contact",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
