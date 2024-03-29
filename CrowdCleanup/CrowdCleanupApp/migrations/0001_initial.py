# Generated by Django 5.0.2 on 2024-02-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('status', models.CharField(choices=[('to_be_cleaned', 'TO BE CLEANED'), ('cleaned', 'CLEANED')], default='to_be_cleaned', max_length=13)),
                ('description', models.TextField()),
            ],
        ),
    ]
