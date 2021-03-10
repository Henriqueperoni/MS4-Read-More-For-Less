from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_club, name='book_club'),
    path(
        'view_review/<int:review_id>/', views.view_review, name='view_review'),
    path('create_review/', views.create_review, name='create_review'),
    path(
        'edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]
