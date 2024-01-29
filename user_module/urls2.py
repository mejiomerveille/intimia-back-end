from django.urls import path 
from .views2 import CurrentUserView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login',),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('get/', CurrentUserView.as_view(), name='current_user'),
]