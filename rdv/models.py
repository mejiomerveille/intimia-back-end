from django.db import models
from grossesse.models import Grossesse
from django.utils.text import slugify
from django.core.validators import EmailValidator
from user_module.models import CustomUser


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])

# mervcodemerveille
class RendezVous(models.Model):
    grossesse = models.ForeignKey(Grossesse, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    date = models.DateField()
    time = models.TimeField()
    weight = models.IntegerField()
    reminder = models.BooleanField()
    notes = models.TextField(blank=True)
    file = models.FileField(blank=True,default="null")
    file_name = models.CharField(max_length=255, blank=True)
