# Generated by Django 3.0.5 on 2020-05-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_auto_20200509_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='link',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Link:'),
        ),
    ]
