from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('photo/upload/', views.photo_upload, name='photo_upload'),
]