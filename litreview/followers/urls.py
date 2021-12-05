from django.urls import path
from . import views

urlpatterns=[
    path('followers/', views.followers, name='followers'),
]