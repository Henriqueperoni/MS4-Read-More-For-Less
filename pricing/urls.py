
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans_pricing, name='pricing'),
    path('add/', views.add_pricing, name='add_pricing'),
]
