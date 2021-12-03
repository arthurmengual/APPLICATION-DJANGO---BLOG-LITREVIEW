from . import views
from django.urls import path

urlpatterns = [
    path('flux/', views.flux, name='flux'),
    path('ticket/create', views.create_ticket, name='create_ticket'),
    path('review/create', views.create_review, name='create_review'),
    path('edit/<int:ticket_id>/ticket/', views.edit_ticket, name='edit_ticket')
]