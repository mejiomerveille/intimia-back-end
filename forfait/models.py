from django.db import models

from grossesse.models import Grossesse
from blog.models import CreateBlog
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
    Grossesse_forfait =models.ForeignKey(Grossesse,on_delete=models.CASCADE)
    blog_forfait =models.ForeignKey(CreateBlog,on_delete=models.CASCADE)