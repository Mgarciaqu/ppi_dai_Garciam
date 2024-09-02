from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('profile/', views.user_profile, name='user_profile'),
    path('cart/', views.cart, name='cart'),
]
