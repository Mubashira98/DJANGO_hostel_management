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
    date_of_birth = models.DateField()
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
    hostel_image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.hostel_name

class Food(models.Model):
    breakfast = models.CharField(max_length=500)
    lunch = models.CharField(max_length=500)
    snacks = models.CharField(max_length=500)
    dinner = models.CharField(max_length=500)

    def __str__(self):
        return self.breakfast

class Fee(models.Model):
    Student_name = models.CharField(max_length=250)
    registration_id = models.CharField(max_length=250)
    from_date = models.DateField()
    to_date = models.DateField()
    mess_bill = models.IntegerField()
    room_rent = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=200)
    paid_date = models.DateField()
    paid_by = models.CharField(max_length=200)

    def __str__(self):
        return self.registration_id

class Notification(models.Model):
    notification = models.CharField(max_length=500)
    date = models.DateField()
    to = models.CharField(max_length=100)

    def __str__(self):
        return self.notification

class Attendance(models.Model):
    name = models.ForeignKey(Student_register,on_delete=models.CASCADE)
    registration_id = models.CharField(max_length=150)
    date = models.DateField()
    attendance_status = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Complaint(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    complaint = models.TextField(max_length=1000)
    reply = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=200)
    registration_id = models.CharField(max_length=200)
    card_no = models.IntegerField()
    expiry_date = models.DateField()
    cvv = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.registration_id

class Review(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    review = models.TextField(max_length=600)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=200)
    email_id =models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name

class Room_booking(models.Model):
    name = models.CharField(max_length=200)
    joining_date = models.DateField()
    booking_date = models.DateField()
    booking_status = models.IntegerField(default=0)

    def __str__(self):
        return self.name



