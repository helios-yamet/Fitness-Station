from django.urls import path
from . import views

urlpatterns = [
    path(r'^enquiries/$', views.enquiries, name='enquiries'),
]
