# Generated by Django 5.1.3 on 2024-12-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_system', '0007_alter_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Запланировано'), ('completed', 'Завершено'), ('missed', 'Сгорело'), ('rescheduled', 'Перенесено')], max_length=50),
        ),
    ]
