from django.db import models
from user_module.models import CustomUser
from grossesse.models import Grossesse

class Notes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='note_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    grossesse = models.ForeignKey(Grossesse, on_delete=models.CASCADE)

    def __str__(self):
        return self.title