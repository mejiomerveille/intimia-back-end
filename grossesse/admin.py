from django.contrib import admin

# Register your models here.
from .models import InfoGrossesse, Grossesse, WeightWoman

admin.site.register(InfoGrossesse)
admin.site.register(Grossesse)
admin.site.register(WeightWoman)
