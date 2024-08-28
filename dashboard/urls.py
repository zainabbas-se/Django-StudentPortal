# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.semester_registration, name='semester_registration'),
    # Other URL patterns
]
