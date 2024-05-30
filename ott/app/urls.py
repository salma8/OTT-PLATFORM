from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import admin_dashboard, user_login, logout_confirmation, subscription

urlpatterns = [
    path('admindash/', admin_dashboard, name='admin-dashboard'),
    path('', user_login, name='login'),
    path('logout/', logout_confirmation, name='logout'),
    path('subscription/',subscription, name='subscription')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)