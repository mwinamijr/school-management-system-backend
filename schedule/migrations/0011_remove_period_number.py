# Generated by Django 3.1.2 on 2021-05-07 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20210503_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='number',
        ),
    ]