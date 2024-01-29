from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self) -> str:
        return self.username