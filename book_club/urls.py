from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_club, name='book_club'),
    path(
        'view_review/<int:review_id>/', views.view_review, name='view_review'),
]
