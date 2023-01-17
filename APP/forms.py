import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from APP.models import Student_register, Parent_register, Login_view, Hostel, Food, Notification, Attendance, \
    Complaint, Payment, Review, Staff, Room_booking, Fee


class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('this is not a valid phone number')

class userregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class StudentForm(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',message='Please enter a Valid Email')])
    date_of_birth = forms.DateField(widget=DateInput)
    class Meta:
        model = Student_register
        exclude = ("user","approval_status")
def clean_email(self):
    mail = self.cleaned_data["email"]
    parent_email = Parent_register.objects.filter(email=mail)
    student_email = Student_register.objects.filter(email=mail)
    if parent_email.exists():
        raise forms.ValidationError("this email is already registered")
    if student_email.exists():
        raise forms.ValidationError("this email is already registered")
    return  mail


def clean_phone_no(self):
    phone = self.cleaned_data["email"]
    parent_phone_no = Parent_register.objects.filter(phone=phone)
    student_phone_no = Student_register.objects.filter(phone=phone)
    if parent_phone_no.exists():
        raise forms.ValidationError("this email is already registered")
    if student_phone_no.exists():
        raise forms.ValidationError("this email is already registered")
    return phone

class Parentform(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please enter a Valid Email')])
    class Meta:
        model = Parent_register
        fields = "__all__"
        exclude = ("user","approval_status")

class hostel_form(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = "__all__"

class food_form(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class fee_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Fee
        fields = "__all__"

class payment_form(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ("status",)


class notification_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Notification
        fields = "__all__"

att_choice = (
    ('present','present'),
    ('absent','absent')
)
class attendance_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    attendance_status = forms.ChoiceField(choices=att_choice,widget=forms.RadioSelect)
    class Meta:
        model = Attendance
        exclude = ('registration_id',)



class complaint_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Complaint

        fields = "__all__"
        exclude = ("reply",)

class reply_form(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"
        exclude = ("complaint", "date","name",)



class review_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Review
        fields = "__all__"

class staff_form(forms.ModelForm):
    email_id = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please enter a Valid Email')])
    class Meta:
        model = Staff
        fields = "__all__"

class roombooking_form(forms.ModelForm):
    joining_date = forms.DateField(widget=DateInput)
    booking_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Room_booking
        fields = "__all__"
        exclude = ('booking_status',)


