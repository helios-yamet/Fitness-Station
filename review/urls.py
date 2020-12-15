from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.Review, name='review'),
]
