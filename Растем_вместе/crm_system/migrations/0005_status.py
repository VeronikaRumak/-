# Generated by Django 5.1.3 on 2024-12-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_system', '0004_position_employee_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
