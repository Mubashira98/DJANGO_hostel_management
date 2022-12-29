import datetime

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
    Student_name = forms.ModelChoiceField(queryset=Student_register.objects.filter(approval_status=True))
    from_date = forms.DateField()
    to_date = forms.DateField()
    room_rent = forms.CharField()

    mess_bill = forms.CharField()


    class Meta:
        model = Fee
        fields = ('Student_name', 'from_date', 'to_date', 'room_rent', 'mess_bill')

    # ajax
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if (from_date > datetime.date.today()):
            raise forms.ValidationError("Invalid From Date")
        if to_date <= from_date or to_date > datetime.date.today():
            raise forms.ValidationError("Invalid To Date")

        from_day = from_date.strftime("%d")
        from_m = from_date.strftime("%m")
        to_day = to_date.strftime("%d")
        print(from_m, to_day)

        if int(from_day) != 1:
            raise forms.ValidationError('Invalid From Date')
        if int(from_m) == 2:
            if int(to_day) not in [29, 28]:
                raise forms.ValidationError('Invalid To Date')

        else:

            if int(from_m) in [1, 3, 5, 7, 8, 10, 12]:
                if int(to_day) != 31:
                    raise forms.ValidationError('Invalid To Date')

            elif int(from_m) == [4, 6, 9, 11]:

                if int(to_day) != 30:
                    raise forms.ValidationError('Invalid To Date')

        return cleaned_data

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


