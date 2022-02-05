# Generated by Django 4.0.2 on 2022-02-05 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_branch_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=240)),
                ('Branch_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='superadmin.branch')),
            ],
        ),
    ]
