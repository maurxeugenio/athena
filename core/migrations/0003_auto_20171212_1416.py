# Generated by Django 2.0 on 2017-12-12 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171208_2124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheduling',
            options={'verbose_name': 'agendamento', 'verbose_name_plural': 'agendamentos'},
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='date',
            field=models.DateField(verbose_name='dia da consulta'),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='end_time',
            field=models.TimeField(max_length=20, verbose_name='fim'),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='patient',
            field=models.CharField(max_length=20, verbose_name='paciente'),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='procedure',
            field=models.CharField(max_length=30, verbose_name='procedimento'),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='start_time',
            field=models.TimeField(max_length=20, verbose_name='inicio'),
        ),
    ]
