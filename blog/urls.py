from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blog'

""" Registering URL adresses for catalog app"""
urlpatterns = [
      path('blog_list/', BlogListView.as_view() , name='blog_list'),
      path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]