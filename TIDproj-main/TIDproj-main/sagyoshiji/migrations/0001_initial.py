# Generated by Django 5.1.2 on 2024-11-19 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_order_number', models.PositiveIntegerField(unique=True, verbose_name='作業指示票番号')),
                ('work_number', models.CharField(max_length=20, verbose_name='工番')),
                ('subject', models.CharField(max_length=20, verbose_name='件名')),
                ('process_pattern', models.CharField(max_length=10, verbose_name='製造工程パタン')),
                ('manager', models.CharField(max_length=20, verbose_name='製造管理担当者')),
                ('work_hours', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='作業工数時間')),
                ('next_process', models.CharField(max_length=20, verbose_name='次工程')),
                ('start_date', models.DateField(verbose_name='作業開始日')),
                ('end_date', models.DateField(verbose_name='終了予定日')),
            ],
            options={
                'verbose_name': '作業指示票',
                'verbose_name_plural': '作業指示票',
            },
        ),
    ]
