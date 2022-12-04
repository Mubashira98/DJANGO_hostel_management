from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from APP.forms import userregister, StudentForm, Parentform


# Create your views here.
def mainpage(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin1')
            elif user.is_student:
                if user.student.approval_status == True:
                    login(request,user)
                return redirect('studentview')
            elif user.is_parent:
                return redirect('parentview')
        else:
            messages.info(request,"invalid credentials")
    return render(request,'index.html')

# student registration form
def student(request):
    u_form = userregister()
    s_form = StudentForm()
    if request.method == "POST":
        u_form = userregister(request.POST)
        s_form = StudentForm(request.POST)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request,"student registration completed")

            return redirect('mainpage')

    return render(request,'signupstudent.html',{'u_form':u_form,'s_form':s_form})

# parent registration from
def parent(request):
    u_form = userregister()
    p_form = Parentform()
    if request.method == "POST":
        u_form = userregister(request.POST)
        p_form = Parentform(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = p_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request,"parent registration completed")

            return redirect('mainpage')
    return render(request,'signupparent.html',{'u_form':u_form,'p_form':p_form})


def admin1(request):
    return render(request,'admin.html')

def studentview(request):
    return render(request,'student.html')

def parentview(request):
    return render(request,'parent.html')


