from django.urls import path
from . import views

app_name = 'App_blog'
urlpatterns = [
     path('', views.BlogListView.as_view(), name='blog_list'),
     path('write/', views.CreateBlog.as_view(), name='create_blog'),
     path('details/<str:blog_title>', views.blog_details, name='blog_details'),
     path('liked/<pk>/', views.liked, name='liked_post'),
     path('unliked/<pk>/', views.un_liked, name='un_liked'),
     path('myblogs/', views.MyBlogs.as_view(), name='my_blogs'),
     path('edit/<pk>/', views.UpdateBlogs.as_view(), name='edit_blog'),
]