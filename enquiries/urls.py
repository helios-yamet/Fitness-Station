from django.urls import path
from . import views


urlpatterns = [
    path('enquiries/', views.enquiries, name='enquiries'),
]
