from django.urls import path
from .views import ProductsListView, ProductDetailView, ContactsTemplateView, HomeTemplateView

app_name = 'catalog'

""" Registering URL adresses for catalog app"""
urlpatterns = [
      path('home/', HomeTemplateView.as_view(), name='home_template'),
      path('products_list/', ProductsListView.as_view() , name='products_list'),
      path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
      path('contacts/', ContactsTemplateView.as_view(), name='contacts_template'),
]