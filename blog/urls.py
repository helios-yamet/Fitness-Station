from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.get_blog_item, name='get_blog_item'),
    path('add_post', views.add_blog_item, name='add'),
    path('edit/<item_id>', views.edit_item, name = 'edit'),
    path('toggle/<item_id>', views.toggle_item, name = 'toggle'),
    path('delete/<item_id>', views.delete_item, name='delete'),
]
