from django.db import models
from grossesse.models import Grossesse

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date = models.DateField(auto_now_add=True)
    pregnancy = models.ForeignKey(Grossesse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name