# Generated by Django 3.2.25 on 2024-07-17 14:40

from django.db import migrations, models
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osidb', '0156_flaw_bzsync_manager_field'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='flaw',
            name='insert_insert',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='flaw',
            name='update_update',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='flaw',
            name='delete_delete',
        ),
        migrations.AddField(
            model_name='flaw',
            name='task_updated_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flawaudit',
            name='task_updated_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='flaw',
            trigger=pgtrigger.compiler.Trigger(name='insert_insert', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "osidb_flawaudit" ("acl_read", "acl_write", "bzsync_manager_id", "comment_zero", "components", "created_dt", "cve_description", "cve_id", "cwe_id", "download_manager_id", "group_key", "impact", "major_incident_start_dt", "major_incident_state", "mitigation", "nist_cvss_validation", "owner", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "reported_dt", "requires_cve_description", "source", "statement", "task_key", "task_updated_dt", "team_id", "title", "unembargo_dt", "uuid", "workflow_name", "workflow_state") VALUES (NEW."acl_read", NEW."acl_write", NEW."bzsync_manager_id", NEW."comment_zero", NEW."components", NEW."created_dt", NEW."cve_description", NEW."cve_id", NEW."cwe_id", NEW."download_manager_id", NEW."group_key", NEW."impact", NEW."major_incident_start_dt", NEW."major_incident_state", NEW."mitigation", NEW."nist_cvss_validation", NEW."owner", _pgh_attach_context(), NOW(), \'insert\', NEW."uuid", NEW."reported_dt", NEW."requires_cve_description", NEW."source", NEW."statement", NEW."task_key", NEW."task_updated_dt", NEW."team_id", NEW."title", NEW."unembargo_dt", NEW."uuid", NEW."workflow_name", NEW."workflow_state"); RETURN NULL;', hash='88ce22bbdde1b0a3d43aee50fe40e2fa57831df9', operation='INSERT', pgid='pgtrigger_insert_insert_4e668', table='osidb_flaw', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='flaw',
            trigger=pgtrigger.compiler.Trigger(name='update_update', sql=pgtrigger.compiler.UpsertTriggerSql(condition='WHEN (OLD."acl_read" IS DISTINCT FROM NEW."acl_read" OR OLD."acl_write" IS DISTINCT FROM NEW."acl_write" OR OLD."bzsync_manager_id" IS DISTINCT FROM NEW."bzsync_manager_id" OR OLD."comment_zero" IS DISTINCT FROM NEW."comment_zero" OR OLD."components" IS DISTINCT FROM NEW."components" OR OLD."created_dt" IS DISTINCT FROM NEW."created_dt" OR OLD."cve_description" IS DISTINCT FROM NEW."cve_description" OR OLD."cve_id" IS DISTINCT FROM NEW."cve_id" OR OLD."cwe_id" IS DISTINCT FROM NEW."cwe_id" OR OLD."download_manager_id" IS DISTINCT FROM NEW."download_manager_id" OR OLD."group_key" IS DISTINCT FROM NEW."group_key" OR OLD."impact" IS DISTINCT FROM NEW."impact" OR OLD."major_incident_start_dt" IS DISTINCT FROM NEW."major_incident_start_dt" OR OLD."major_incident_state" IS DISTINCT FROM NEW."major_incident_state" OR OLD."mitigation" IS DISTINCT FROM NEW."mitigation" OR OLD."nist_cvss_validation" IS DISTINCT FROM NEW."nist_cvss_validation" OR OLD."owner" IS DISTINCT FROM NEW."owner" OR OLD."reported_dt" IS DISTINCT FROM NEW."reported_dt" OR OLD."requires_cve_description" IS DISTINCT FROM NEW."requires_cve_description" OR OLD."source" IS DISTINCT FROM NEW."source" OR OLD."statement" IS DISTINCT FROM NEW."statement" OR OLD."task_key" IS DISTINCT FROM NEW."task_key" OR OLD."task_updated_dt" IS DISTINCT FROM NEW."task_updated_dt" OR OLD."team_id" IS DISTINCT FROM NEW."team_id" OR OLD."title" IS DISTINCT FROM NEW."title" OR OLD."unembargo_dt" IS DISTINCT FROM NEW."unembargo_dt" OR OLD."uuid" IS DISTINCT FROM NEW."uuid" OR OLD."workflow_name" IS DISTINCT FROM NEW."workflow_name" OR OLD."workflow_state" IS DISTINCT FROM NEW."workflow_state")', func='INSERT INTO "osidb_flawaudit" ("acl_read", "acl_write", "bzsync_manager_id", "comment_zero", "components", "created_dt", "cve_description", "cve_id", "cwe_id", "download_manager_id", "group_key", "impact", "major_incident_start_dt", "major_incident_state", "mitigation", "nist_cvss_validation", "owner", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "reported_dt", "requires_cve_description", "source", "statement", "task_key", "task_updated_dt", "team_id", "title", "unembargo_dt", "uuid", "workflow_name", "workflow_state") VALUES (NEW."acl_read", NEW."acl_write", NEW."bzsync_manager_id", NEW."comment_zero", NEW."components", NEW."created_dt", NEW."cve_description", NEW."cve_id", NEW."cwe_id", NEW."download_manager_id", NEW."group_key", NEW."impact", NEW."major_incident_start_dt", NEW."major_incident_state", NEW."mitigation", NEW."nist_cvss_validation", NEW."owner", _pgh_attach_context(), NOW(), \'update\', NEW."uuid", NEW."reported_dt", NEW."requires_cve_description", NEW."source", NEW."statement", NEW."task_key", NEW."task_updated_dt", NEW."team_id", NEW."title", NEW."unembargo_dt", NEW."uuid", NEW."workflow_name", NEW."workflow_state"); RETURN NULL;', hash='6aba09b317379817f2c99d79093d31c105948b9b', operation='UPDATE', pgid='pgtrigger_update_update_96595', table='osidb_flaw', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='flaw',
            trigger=pgtrigger.compiler.Trigger(name='delete_delete', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "osidb_flawaudit" ("acl_read", "acl_write", "bzsync_manager_id", "comment_zero", "components", "created_dt", "cve_description", "cve_id", "cwe_id", "download_manager_id", "group_key", "impact", "major_incident_start_dt", "major_incident_state", "mitigation", "nist_cvss_validation", "owner", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "reported_dt", "requires_cve_description", "source", "statement", "task_key", "task_updated_dt", "team_id", "title", "unembargo_dt", "uuid", "workflow_name", "workflow_state") VALUES (OLD."acl_read", OLD."acl_write", OLD."bzsync_manager_id", OLD."comment_zero", OLD."components", OLD."created_dt", OLD."cve_description", OLD."cve_id", OLD."cwe_id", OLD."download_manager_id", OLD."group_key", OLD."impact", OLD."major_incident_start_dt", OLD."major_incident_state", OLD."mitigation", OLD."nist_cvss_validation", OLD."owner", _pgh_attach_context(), NOW(), \'delete\', OLD."uuid", OLD."reported_dt", OLD."requires_cve_description", OLD."source", OLD."statement", OLD."task_key", OLD."task_updated_dt", OLD."team_id", OLD."title", OLD."unembargo_dt", OLD."uuid", OLD."workflow_name", OLD."workflow_state"); RETURN NULL;', hash='a45a3ecf173cfcd245d012f9ed02d8599e2b04a6', operation='DELETE', pgid='pgtrigger_delete_delete_f2e13', table='osidb_flaw', when='AFTER')),
        ),
    ]
