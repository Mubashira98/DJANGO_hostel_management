from django import forms
from django.contrib.auth.forms import UserCreationForm

from APP.models import Student_register, Parent_register, Login_view, Hostel, Food, Fee, Notification, Attendance, \
    Complaint, Payment, Review, Staff, Room_booking

class DateInput(forms.DateInput):
    input_type = 'date'


class userregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput)
    class Meta:
        model = Student_register
        fields = "__all__"
        exclude = ("user","approval_status")

class Parentform(forms.ModelForm):
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
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    paid_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Fee
        fields = "__all__"

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

class payment_form(forms.ModelForm):
    expiry_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        fields = "__all__"

class review_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Review
        fields = "__all__"

class staff_form(forms.ModelForm):
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

