# Generated by Django 3.0.5 on 2020-05-10 05:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0011_auto_20200510_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date From: '),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date To: '),
        ),
    ]