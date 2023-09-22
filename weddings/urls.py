# weddings/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('folders/', views.folder_list, name='folder_list'),
    path('folders/<int:folder_id>/', views.image_list, name='image_list'),
    path('images/<int:image_id>/', views.image_detail, name='image_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('download/<int:image_id>/', views.download_image, name='download_image'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


