# Generated by Django 3.2.25 on 2024-08-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osidb', '0158_remove_tracker_unique_together'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='tracker',
            constraint=models.UniqueConstraint(condition=models.Q(('external_system_id', ''), _negated=True), fields=('type', 'external_system_id'), name='unique_external_system_id'),
        ),
    ]