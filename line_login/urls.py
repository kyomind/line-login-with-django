from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login', views.log_in, name='log-in'),
    path('logout', views.log_out, name='log-out'),
]