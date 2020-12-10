from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
]
