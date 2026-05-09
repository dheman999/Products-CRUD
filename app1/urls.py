from django.urls import path
from . import views



urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products_list, name='products_list'),
    path('products/add/', views.add_products, name='add_products'),
    path('products/update/<int:pk>/', views.update_products, name='update_products'),
    path('products/delete/<int:pk>/', views.delete_products, name='delete_products'),

]