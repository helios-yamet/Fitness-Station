from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post', views.add_blog_post, name='add_blog_post'),
    path('edit/<item_id>', views.edit_blog_item, name='edit_blog_item'),
    path('delete/<item_id>', views.delete_item, name='delete'),
]
