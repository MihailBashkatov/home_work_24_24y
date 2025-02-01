from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

""" Registering URL adresses for catalog app"""
urlpatterns = [
      path('blog_list/', BlogListView.as_view() , name='blog_list'),
      path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
      path('blog_create', BlogCreateView.as_view(), name='blog_create'),
      path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
      path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]