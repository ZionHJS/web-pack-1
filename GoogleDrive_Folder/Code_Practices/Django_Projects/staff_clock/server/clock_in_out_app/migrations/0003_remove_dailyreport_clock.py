# Generated by Django 2.2 on 2019-12-22 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clock_in_out_app', '0002_auto_20191222_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='clock',
        ),
    ]
