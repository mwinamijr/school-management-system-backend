# Generated by Django 3.1.8 on 2021-06-17 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0015_period_taught'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ('id', 'period_time')},
        ),
    ]
