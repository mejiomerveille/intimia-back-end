# Generated by Django 4.2.4 on 2024-02-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grossesse', '0004_remove_informationgrossesse_id_and_more'),
        ('symptoms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='pregnancy',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='grossesse.grossesse'),
            preserve_default=False,
        ),
    ]
