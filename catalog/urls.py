from django.urls import path
from . import views

app_name = 'catalog'

""" Registering URL adresses for catalog app"""
urlpatterns = [
    # path('show_data/', views.show_data, name='show_data'),
    # path('submit_data/', views.submit_data, name='submit_data'),
    # path('item/<int:item_id/>', views.show_item, name='show_item'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    # path('contact/', views.contact, name='contact'),
]