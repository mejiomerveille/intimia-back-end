# Generated by Django 4.2.4 on 2024-02-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grossesse', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationGrossesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semaine', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='InfoGrossesse',
        ),
    ]
