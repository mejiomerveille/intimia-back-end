from django.db import models
from user_module.models import CustomUser

class Conversation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role_choices = [
        ('user', 'User'),
        ('assistant', 'Assistant')
    ]
    role = models.CharField(max_length=10, choices=role_choices)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    create_at=models.DateField(auto_now_add=True)
    create_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="make_by",default=None,null=True)
    modify_at=models.DateField(auto_now_add=True)
    modify_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="change_by",default=None,null=True)
