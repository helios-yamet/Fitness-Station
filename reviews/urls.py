from django.urls import path
from blog import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('add_review', views.add_review_post, name='add_review'),
]
