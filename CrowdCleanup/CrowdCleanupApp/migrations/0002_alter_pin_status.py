# Generated by Django 5.0.2 on 2024-02-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrowdCleanupApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='status',
            field=models.CharField(default='TO BE CLEANED', max_length=13),
        ),
    ]