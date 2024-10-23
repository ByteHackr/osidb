# Generated by Django 4.2.16 on 2024-10-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("osidb", "0169_psupdatestream_moderate_to_ps_module"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flaw",
            name="major_incident_state",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Novalue"),
                    ("REQUESTED", "Requested"),
                    ("REJECTED", "Rejected"),
                    ("APPROVED", "Approved"),
                    ("CISA_APPROVED", "Cisa Approved"),
                    ("MINOR", "Minor"),
                    ("ZERO_DAY", "Zero Day"),
                    ("INVALID", "Invalid"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="flawaudit",
            name="major_incident_state",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Novalue"),
                    ("REQUESTED", "Requested"),
                    ("REJECTED", "Rejected"),
                    ("APPROVED", "Approved"),
                    ("CISA_APPROVED", "Cisa Approved"),
                    ("MINOR", "Minor"),
                    ("ZERO_DAY", "Zero Day"),
                    ("INVALID", "Invalid"),
                ],
                max_length=20,
            ),
        ),
    ]