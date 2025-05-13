# appl/models.py
from django.db import models

class Employee(models.Model):
    empno = models.IntegerField(unique=True)
    empname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.empname} ({self.empno})"
