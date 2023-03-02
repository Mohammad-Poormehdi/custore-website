from django.urls import path
from cms import views

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('customers/', views.customers, name='customers'),
    path('orders', views.orders, name='orders')
]
