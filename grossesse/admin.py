from django.contrib import admin

# Register your models here.
from .models import InformationGrossesse, Grossesse, WeightWoman

admin.site.register(InformationGrossesse)
admin.site.register(Grossesse)
admin.site.register(WeightWoman)
