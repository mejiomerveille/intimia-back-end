# Generated by Django 4.2.4 on 2024-03-13 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forfait', '0002_remove_forfait_grossesse_forfait_and_more'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createblog',
            name='blog_forfait',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forfait.forfait'),
        ),
    ]