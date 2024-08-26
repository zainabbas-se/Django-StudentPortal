from django.urls import path
from . import views

urlpatterns = [
    path('adding', views.adding, name='adding'),
    # Add more URL patterns here
]
