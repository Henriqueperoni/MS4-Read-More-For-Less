
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]
