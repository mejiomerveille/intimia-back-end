# Generated by Django 4.2.4 on 2024-02-26 10:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grossesse', '0006_alter_grossesse_create_by_alter_grossesse_modify_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rdv', '0005_doctors_rendezvou_delete_doctor_delete_rendezvous'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RendezVou',
            new_name='RendezVous',
        ),
    ]
