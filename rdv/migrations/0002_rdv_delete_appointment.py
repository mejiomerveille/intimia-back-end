# Generated by Django 4.2.4 on 2024-02-04 20:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grossesse', '0002_initial'),
        ('rdv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RDV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('weight', models.IntegerField()),
                ('reminder', models.BooleanField()),
                ('notes', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, default='null', upload_to='')),
                ('file_name', models.CharField(blank=True, max_length=255)),
                ('grossesse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grossesse.grossesse')),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
