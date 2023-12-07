# Generated by Django 3.2.20 on 2023-11-10 16:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("osidb", "0108_osim_renamed"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompliancePriority",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("ps_module", models.CharField(max_length=100)),
                ("ps_component", models.CharField(max_length=255)),
            ],
        ),
    ]
