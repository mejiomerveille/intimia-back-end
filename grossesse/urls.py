from django.urls import path
from .views import *

urlpatterns = [
    path('register-grossesse/', registerGrossesse, name='regis_grossesse'),
    path('semaine/', current_week, name='semaine'),
]
