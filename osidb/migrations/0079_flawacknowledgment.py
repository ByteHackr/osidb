# Generated by Django 3.2.19 on 2023-06-22 17:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import psqlextra.fields.hstore_field
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('osidb', '0078_flaw_major_incident_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlawAcknowledgment',
            fields=[
                ('created_dt', models.DateTimeField(blank=True)),
                ('updated_dt', models.DateTimeField(blank=True)),
                ('_alerts', models.JSONField(blank=True, default=dict)),
                ('acl_read', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None)),
                ('acl_write', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('affiliation', models.CharField(max_length=255)),
                ('from_upstream', models.BooleanField()),
                ('meta_attr', psqlextra.fields.hstore_field.HStoreField(default=dict)),
                ('flaw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acknowledgments', to='osidb.flaw')),
            ],
            options={
                'unique_together': {('flaw', 'name', 'affiliation')},
            },
        ),
    ]
