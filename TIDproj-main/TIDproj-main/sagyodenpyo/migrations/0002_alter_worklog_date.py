# Generated by Django 5.1.2 on 2024-11-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyodenpyo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='date',
            field=models.DateField(verbose_name='作業日'),
        ),
    ]
