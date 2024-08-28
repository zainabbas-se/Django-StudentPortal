# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.semester_registration, name='semester_registration'),

    path('delete_semester/<int:id>/', views.delete_semester, name='delete_semester'),
    path('update_semester/<int:id>/', views.update_semester, name='update_semester'),
    # Other URL patterns
]
