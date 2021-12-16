from . import views
from django.urls import path, include

urlpatterns = [
    path('flux/', views.flux, name='flux'),
    path('ticket/create', views.create_ticket, name='create_ticket'),
    path('review/create', views.create_review, name='create_review'),
    path('edit/<int:ticket_id>/ticket/', views.edit_ticket, name='edit_ticket'),
    path('edit/<int:review_id>/review/', views.edit_review, name='edit_review'),
    path('posts/', views.posts, name='posts'),
    path('review/to/ticket/<int:ticket_id>/',
         views.review_to_ticket, name='review_to_ticket'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
