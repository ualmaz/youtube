# Generated by Django 3.0.5 on 2020-05-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0013_auto_20200510_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='content',
            field=models.CharField(default='', max_length=20, verbose_name='Content:'),
        ),
    ]
