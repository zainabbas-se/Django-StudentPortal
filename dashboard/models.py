from django.db import models
from django.contrib.auth.models import User


class Semester(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.department} - {self.semester}"
