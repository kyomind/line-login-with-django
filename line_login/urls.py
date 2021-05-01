from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('login/', views.),
    # path('logout', views.main),
    # path('', views.suv_main, name='suv-main'),
    # path('suv-search/', views.suv_search, name='suv-search'),
    # path('user/<int:member_id>', views.user_page, name='suv-user'),
]