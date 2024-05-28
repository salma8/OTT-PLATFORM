from django.contrib.auth.views import LoginView
from django.urls import path
from .views import admin_dashboard, user_login

urlpatterns = [
    path('admindash/', admin_dashboard, name='admin-dashboard'),
    path('', user_login, name='login')
]
