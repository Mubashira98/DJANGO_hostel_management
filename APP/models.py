from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

class Student_register(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student')
    name = models.CharField(max_length=250)
    registration_id = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    date_of_birth = models.DateField(auto_now=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    approval_status = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Parent_register(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=250)
    student_name=models.CharField(max_length=250)
    registration_id = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.registration_id

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    Fee_details = models.CharField(max_length=25)
    total_rooms = models.IntegerField()
    room_facilities = models.CharField(max_length=250)
    contact_number = models.IntegerField()
    # hostel_image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.hostel_name