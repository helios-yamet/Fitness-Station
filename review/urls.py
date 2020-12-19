from django.urls import path
from . import views


urlpatterns = [
    path('<product_id>/', views.view_review, name='view_review'),
    path('review_form/<product_id>/', views.review_form, name='review_form'),
]
