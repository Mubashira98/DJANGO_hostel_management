import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.datetime_safe import date

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
            raise forms.ValidationError("this phone no is already registered")
        if student_phone_no.exists():
            raise forms.ValidationError("this phone no is already registered")
        return phone




class Parentform(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please enter a Valid Email')])
    class Meta:
        model = Parent_register
        fields = "__all__"
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
        phone = self.cleaned_data["phone"]
        parent_phone_no = Parent_register.objects.filter(phone=phone)
        student_phone_no = Student_register.objects.filter(phone=phone)
        if parent_phone_no.exists():
            raise forms.ValidationError("this phone no is already registered")
        if student_phone_no.exists():
            raise forms.ValidationError("this phone no is already registered")
        return phone


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

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")
        if from_date > to_date:
            raise forms.ValidationError("to_date should be greater than from_date")


class notification_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Notification
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date != date.today():
            raise forms.ValidationError("date should be today")


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

def clean(self):
    cleaned_data = super().clean()
    date = cleaned_data.get("date")
    if date != date.today():
        raise forms.ValidationError("date should be today")


class complaint_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Complaint

        fields = "__all__"
        exclude = ("reply",)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date != date.today():
            raise forms.ValidationError("date should be today")

class reply_form(forms.ModelForm):

    class Meta:
        model = Complaint

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

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get("booking_date")
        joining_date = cleaned_data.get("joining_date")
        if joining_date < booking_date:
            raise forms.ValidationError("joining_date should be greater than booking_date")
        if booking_date is date.today():
            raise forms.ValidationError("booking_date should be today")
