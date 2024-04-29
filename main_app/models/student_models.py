from typing import Any
from django.db import models
from django.urls import reverse

class Student_info(models.Model):
    name = models.CharField(max_length= 50)
    facebook = models.CharField(max_length= 240, blank = True)
    email = models.EmailField(max_length= 100, blank = True)
    phone = models.CharField(max_length= 100, blank = True)
    blood = models.CharField(max_length= 15, blank = True)
    detail = models.TextField(max_length= 400, blank = True)
    image = models.ImageField(upload_to= 'image/%y', blank = True)



 
    def __str__(self):
        return self.name 

    @staticmethod
    def get_student_data():
        return Student_info.objects.all()

             
    