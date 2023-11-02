from django.db import models

# Create your models here.
from user_module.models import CustomUser as User
import datetime

class InfoGrossesse(models.Model):
    semaine = models.JSONField()


class Grossesse(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f"Grossesse {self.start_date} - {self.end_date}"
    
    def calculer_date_accouchement(self):
        return self.start_date + datetime.timedelta(days=280)
    
    def get_start_date(self):
        return self.start_date

    def save(self, *args, **kwargs):
        self.end_date = self.calculer_date_accouchement()
        super().save(*args, **kwargs)



class WeightWoman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

