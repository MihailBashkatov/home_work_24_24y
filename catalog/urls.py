from django.urls import path
from . import views

app_name = 'catalog'

""" Registering URL adresses for catalog app"""
urlpatterns = [
      path('home/', views.home, name='home'),
      path('contacts/', views.contacts, name='contacts'),
      path('index/<product_id>/', views.index, name='index'),
      path('products_list/', views.products_list, name='products_list'),

]