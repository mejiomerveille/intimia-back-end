from django.urls import path
from .views import *


urlpatterns = [
    path('semaine/<int:num_semaine>/', SemaineView.as_view(), name='semaine_view'),
    path('register/', Grossesses.as_view(), name='regis_grossesse'),
    path('list/',get_all_grossesse , name='liste_grossesse'),
    path('week/',principal , name='week_grossesse'),
    path('edit/<int:grossesse_id>/',modifier_grossesse, name='edit_grossesse'),
    path('current_week/<int:grossesse_id>/',weekView.as_view(), name='recuperer_grossesse'),
]
