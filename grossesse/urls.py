from django.urls import path
from .views import *

urlpatterns = [
    path('regis-grossesse/', registerGrossesse, name='regis_grossesse'),
    path('register-grossesse/', RegisterGrossesseView.as_view(), name='register_grossesse'),
    path('semaine/', current_week, name='semaine'),
    path('',principal , name='principal'),
    path('list_grossesse/',grossesse_list , name='liste_grossesse'),
    path('get-grossesse/', GrossesseListView.as_view(), name='get_grossesse'),
    path('record/', record_data, name='record_data'),
    path('data-list/', data_list, name='data_list'),
    path('edit-data/<int:pk>/',edit_data, name='edit_data'),
    path('delete-data/<int:pk>/', delete_data, name='delete_data'),
    path('edit-grossesse/<int:grossesse_id>/',modifier_grossesse, name='edit_grossesse'),

]
