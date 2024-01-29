from django.urls import path
from .views import *


urlpatterns = [
    path('semaine/<int:num_semaine>/', SemaineView.as_view(), name='semaine_view'),
    path('register/', RegisterView.as_view(), name='regis_grossesse'),
    path('list/',grossesse_list , name='liste_grossesse'),
    path('edit/<int:grossesse_id>/',modifier_grossesse, name='edit_grossesse'),
]
