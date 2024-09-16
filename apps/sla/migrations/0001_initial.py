# Generated by Django 3.2.25 on 2024-08-06 09:35

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SLA",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("duration", models.IntegerField()),
                (
                    "duration_type",
                    models.CharField(
                        choices=[
                            ("Business Days", "Business Days"),
                            ("Calendar Days", "Calendar Days"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "start_criteria",
                    models.CharField(
                        choices=[("Earliest", "Earliest"), ("Latest", "Latest")],
                        max_length=20,
                    ),
                ),
                (
                    "start_dates",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=list,
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SLAPolicy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField()),
                ("condition_descriptions", models.JSONField(default=dict)),
                ("order", models.IntegerField(unique=True)),
                (
                    "sla",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policies",
                        to="sla.sla",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
    ]