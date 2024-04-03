from django.db import models
from user_module.models import CustomUser

# Create your models here.

class Forfait(models.Model):
    type=models.CharField()
    frequence= models.CharField(max_length=50)
    is_active= models.CharField(max_length=50)
    periode= models.CharField(max_length=50)
    unite_de_temps= models.CharField(max_length=50)
    start_date_forfait = models.DateField()
    end_date_forfait = models.DateField()
    date_subscribe = models.DateField()
    categories = models.CharField(default='standard')
    user_forfait =models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    nb_grossesse=models.IntegerField()
    appartenir_a=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="appartenira", default=None,null=True)