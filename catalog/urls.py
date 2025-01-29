from django.urls import path
from .views import ProductsListView, ProductDetailView, ContactsTemplateView, HomeTemplateView, ProductsCreateView, \
      ProductsUpdateView, ProductDeleteView

app_name = 'catalog'

""" Registering URL adresses for catalog app"""
urlpatterns = [
      path('home/', HomeTemplateView.as_view(), name='home_template'),
      path('products/create/', ProductsCreateView.as_view() , name='products_create'),
      path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='products_update'),
      path('products_list/', ProductsListView.as_view() , name='products_list'),
      path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
      path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
      path('contacts/', ContactsTemplateView.as_view(), name='contacts_template'),
]