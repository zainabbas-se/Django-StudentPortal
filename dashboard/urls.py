# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('semester_registration', views.semester_registration, name='semester_registration'),

    path('delete_semester/<int:id>/', views.delete_semester, name='delete_semester'),
    path('update_semester/<int:id>/', views.update_semester, name='update_semester'),
    # Other URL patterns
    path('user_registration', views.user_registration, name='user_registration'),
    path('user_login', views.user_login, name='user_login'),
]

