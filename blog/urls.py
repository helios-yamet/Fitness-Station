from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.AddPostView.as_view(), name='add_post'),
]
