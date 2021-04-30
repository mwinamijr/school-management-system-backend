# Generated by Django 3.1.2 on 2021-04-24 11:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=15, null=True)),
                ('_type', models.CharField(blank=True, choices=[('H', 'Home'), ('C', 'Cell'), ('W', 'Work'), ('O', 'Other')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='emergencycontactnumber',
            name='_type',
        ),
        migrations.RemoveField(
            model_name='emergencycontactnumber',
            name='ext',
        ),
        migrations.RemoveField(
            model_name='emergencycontactnumber',
            name='id',
        ),
        migrations.RemoveField(
            model_name='emergencycontactnumber',
            name='note',
        ),
        migrations.RemoveField(
            model_name='emergencycontactnumber',
            name='number',
        ),
        migrations.AddField(
            model_name='emergencycontactnumber',
            name='phonenumber_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sis.phonenumber'),
            preserve_default=False,
        ),
    ]
