from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Grossesse
from datetime import datetime
from user_module.models import CustomUser
from django.http import request

@receiver(pre_save,sender=Grossesse)
def add_grossesse(sender,instance:Grossesse,**kwargs):
    print("presave create_by")
    if instance.create_by is not None:
        instance.modify_at=datetime.now()
        instance.modify_by=request.user_id
    else:
        instance.create_at=datetime.now()
        instance.create_by=CustomUser.objects.filter(id)

