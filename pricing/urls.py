
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans_pricing, name='pricing'),
    path('<pricing_id>', views.plan_detail, name='plan_detail'),
    path('add/', views.add_plan, name='add_plan'),
    path('edit/<int:pricing_id>/', views.edit_plan, name='edit_plan'),
    path('delete/<int:pricing_id>/', views.delete_plan, name='delete_plan'),
]
