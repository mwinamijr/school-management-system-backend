# Generated by Django 3.1.2 on 2021-05-03 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0006_studentbulkupload'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('addmission_number', 'fname', 'lname'), 'permissions': (('viewStudent', 'View student'), ('reports', 'View reports'))},
        ),
    ]
