from django.urls import path
from . import views
from .views import ProductsListView, ProductDetailView

app_name = 'catalog'

""" Registering URL adresses for catalog app"""
urlpatterns = [
      path('home/', views.home, name='home'),
      path('contacts/', views.contacts, name='contacts'),
      # path('index/<product_id>/', views.index, name='index'),
      # path('products_list/', views.products_list, name='products_list'),
      path('products_list/', ProductsListView.as_view() , name='products_list'),
      path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]