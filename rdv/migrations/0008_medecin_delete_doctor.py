# Generated by Django 4.2.4 on 2024-02-26 10:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rdv', '0007_rename_doctors_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('create_at', models.DateField(auto_now_add=True)),
                ('modify_at', models.DateField(auto_now_add=True)),
                ('create_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crer_par', to=settings.AUTH_USER_MODEL)),
                ('modify_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modifie_par', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
