from django import forms
from django.contrib.auth.forms import UserCreationForm

from APP.models import Student_register, Parent_register, Login_view, Hostel


class userregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class StudentForm(forms.ModelForm):
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