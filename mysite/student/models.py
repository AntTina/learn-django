from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=20) 
    score = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.course
