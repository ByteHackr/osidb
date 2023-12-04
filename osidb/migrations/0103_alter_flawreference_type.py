# Generated by Django 3.2.20 on 2023-11-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osidb', '0102_delete_flawdraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flawreference',
            name='type',
            field=models.CharField(choices=[('ARTICLE', 'Article'), ('EXTERNAL', 'External'), ('SOURCE', 'Source')], default='EXTERNAL', max_length=50),
        ),
    ]