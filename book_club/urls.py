from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_club, name='book_club'),
]
