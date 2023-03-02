from django.urls import path
from custore import views

urlpatterns = [
    path('', views.custore_home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('pages/', views.pages, name='pages'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register')
]
