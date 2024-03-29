# Generated by Django 4.2.4 on 2024-01-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grossesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_finish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InfoGrossesse',
            fields=[
                ('semaine', models.JSONField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WeightWoman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('blood_pressure', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
