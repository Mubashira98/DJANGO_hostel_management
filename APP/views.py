from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from APP.forms import userregister, StudentForm, Parentform, complaint_form, payment_form, \
    review_form, roombooking_form
from APP.models import Hostel, Food, Complaint, Payment, Notification, Attendance, Review, Staff, Room_booking, \
    Student_register, Parent_register, Fee


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
            elif user is not None and user.is_student:
                if user.student.approval_status == True:
                    login(request,user)
                    return redirect('student_profileview')
            elif user is not None and user.is_parent:
                if user.parent.approval_status == True:
                    login(request,user)

                    return redirect('parent_profileview')
        else:
            messages.info(request,"invalid credentials")
    return render(request,'index.html')

# student registration form

def student(request):
    u_form = userregister()
    s_form = StudentForm()
    if request.method == "POST":
        u_form = userregister(request.POST)
        s_form = StudentForm(request.POST,request.FILES)
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

@login_required(login_url='mainpage')
def admin1(request):
    return render(request,'admin.html')

@login_required(login_url='mainpage')
def studentview(request):
    return render(request,'student_dashboard.html')

@login_required(login_url='mainpage')
def parentview(request):
    return render(request,'parent_dashboard.html')

@login_required(login_url='mainpage')
def student_view_hostel(request):
    data = Hostel.objects.all()
    return render(request,'hostel_view.html',{'data':data})

@login_required(login_url='mainpage')
def student_view_food(request):
    data = Food.objects.all()
    return render(request, 'food_view.html', {'data': data})


@login_required(login_url='mainpage')
def add_complaint(request):
    form = complaint_form()
    u = request.user
    if request.method == "POST":
        form = complaint_form(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            form.save()
            return redirect('view_complaint')
    return render(request,'add_a_complaint.html',{'form':form})


@login_required(login_url='mainpage')
def view_complaint(request):
    u = Student_register.objects.get(user=request.user)
    data = Complaint.objects.filter(student_name=u)
    return render(request,'view_complaint.html',{'data':data})


@login_required(login_url='mainpage')
def complaint_update(request,id):
    comp1 = Complaint.objects.get(id=id)
    form = complaint_form(instance=comp1)
    if request.method == 'POST':
        form = complaint_form(request.POST,instance=comp1)
        if form.is_valid():
            form.save()
        return redirect('view_complaint')
    return render(request,'update_complaint.html',{'form':form})

@login_required(login_url='mainpage')
def complaint_delete(request,id):
    Complaint.objects.get(id=id).delete()
    return redirect('view_complaint')

@login_required(login_url='mainpage')
def fee_view(request):
    data = Fee.objects.all()
    return render(request,'fee_view_details.html',{'data':data})

# @login_required(login_url='mainpage')
# def add_payment(request):
#     form = payment_form()
#     if request.method == "POST":
#         form = payment_form(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             if request.GET.get('button') == 'a':
#                 print('submit')
#             return redirect('fee_view')
#     return render(request,'add_payment_details.html',{'form':form})

@login_required(login_url='mainpage')
def view_student_payment(request):
    u = Student_register.objects.get(user=request.user)
    data = Payment.objects.filter(name=u)
    return render(request,'student_view_payment.html',{'data':data})

@login_required(login_url='mainpage')
def approve_payment(request,id):
    pay1 = Payment.objects.get(id=id)
    pay1.status = 1
    pay1.save()
    messages.info(request, 'Student fee paid successfully')
    return redirect('view_student_payment')

def reject_payment(request,id):
    pay1 = Payment.objects.get(id=id)
    pay1.status = 2
    pay1.save()
    messages.info(request, 'Student fee not paid')
    return redirect('view_student_payment')


@login_required(login_url='mainpage')
def notification_view(request):
    data = Notification.objects.all()
    return render(request, 'view_notification_details.html', {'data': data})

@login_required(login_url='mainpage')
def attendance_view(request):
    u = Student_register.objects.get(user=request.user)
    data = Attendance.objects.filter(name=u)
    return render(request, 'view_attendance.html', {'data': data})

@login_required(login_url='mainpage')
def add_review(request):
    form = review_form()
    if request.method == "POST":
        form = review_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_review')
    return render(request,'add_review.html',{'form':form})

@login_required(login_url='mainpage')
def view_review(request):
    data = Review.objects.filter(user=request.user)
    return render(request,'view_review.html',{'data':data})


@login_required(login_url='mainpage')
def update_review(request,id):
    rev1 = Review.objects.get(id=id)
    form = review_form(instance=rev1)
    if request.method == 'POST':
        form = review_form(request.POST,instance=rev1)
        if form.is_valid():
            form.save()
        return redirect('view_review')
    return render(request,'update_review_details.html',{'form':form})


@login_required(login_url='mainpage')
def delete_review(request,id):
    Review.objects.get(id=id).delete()
    return redirect('view_review')


@login_required(login_url='mainpage')
def student_view_staff(request):
    data = Staff.objects.all()
    return render(request, 'student_view_staff.html', {'data': data})


@login_required(login_url='mainpage')
def add_book_room(request):
    form = roombooking_form()
    if request.method == "POST":
        form = roombooking_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_room_booking')
    return render(request, 'book_room.html', {'form': form})


@login_required(login_url='mainpage')
def view_room_booking(request):
    u = Student_register.objects.get(user=request.user)
    data = Room_booking.objects.filter(student_name=u)
    return render(request, 'student_book_room.html', {'data': data})


@login_required(login_url='mainpage')
def update_roombooking(request,id):
    room1 = Room_booking.objects.get(id=id)
    form = roombooking_form(instance=room1)
    if request.method == 'POST':
        form = roombooking_form(request.POST,instance=room1)
        if form.is_valid():
            form.save()
        return redirect('view_room_booking')
    return render(request,'update_roombooking.html',{'form':form})


@login_required(login_url='mainpage')
def delete_roombooking(request,id):
    Room_booking.objects.get(id=id).delete()
    return redirect('view_room_booking')


@login_required(login_url='mainpage')
def student_viewstudents(request):
    data = Student_register.objects.all()
    return render(request,'student_view_student.html',{'data':data})

# parent views

@login_required(login_url='mainpage')
def parent_view_hostel(request):
    data = Hostel.objects.all()
    return render(request,'parent_hostel_view.html',{'data':data})


@login_required(login_url='mainpage')
def parent_view_staff(request):
    data = Staff.objects.all()
    return render(request, 'parent_view_staff.html', {'data': data})


@login_required(login_url='mainpage')
def parent_attendance_view(request):
    u = Parent_register.objects.get(user=request.user)
    data = Attendance.objects.filter(name=u.student_name)
    return render(request, 'parent_view_attendance.html', {'data': data})


@login_required(login_url='mainpage')
def parent_add_payment(request):
    form = payment_form()
    if request.method == "POST":
        form = payment_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parent_view_payment')
    return render(request,'parent_add_payment_details.html',{'form':form})


@login_required(login_url='mainpage')
def parent_view_payment(request):
    u = Parent_register.objects.get(user=request.user)
    data = Payment.objects.filter(name=u.student_name)
    return render(request,'parent_view_payment.html',{'data':data})


@login_required(login_url='mainpage')
def parent_view_fee(request):
    data = Fee.objects.all()
    return render(request, 'parent_view_fee_details.html', {'data': data})


@login_required(login_url='mainpage')
def student_profileview(request):
    student = Student_register.objects.get(user=request.user)
    return render(request,'student_dashboard.html',{'student':student})


@login_required(login_url='mainpage')
def student_updateprofile(request):
    student1 = Student_register.objects.get(user=request.user)
    form = StudentForm(instance=student1)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES, instance=student1)
        if form.is_valid():
            form.save()
        return redirect('student_profileview')
    return render(request, 'student_update_profile.html', {'form': form})

@login_required(login_url='mainpage')
def delete_profile_student(request):
    user = request.user
    print(user)
    if request.method == "POST":
        user.delete()
        messages.info(request, 'Your account deleted successfully')
        return redirect('mainpage')
    return render(request,'delete_account.html')


@login_required(login_url='mainpage')
def logout_view(request):
    logout(request)
    return redirect('mainpage')


@login_required(login_url='mainpage')
def parent_profileview(request):
    parent = Parent_register.objects.get(user=request.user)
    return render(request,'parent_dashboard.html',{'parent':parent})


@login_required(login_url='mainpage')
def parent_updateprofile(request):
    parent1 = Parent_register.objects.get(user=request.user)
    form = Parentform(instance=parent1)
    if request.method == 'POST':
        form = Parentform(request.POST,request.FILES, instance=parent1)
        if form.is_valid():
            form.save()
        return redirect('parent_profileview')
    return render(request, 'parent_updateprofile.html', {'form': form})

@login_required(login_url='mainpage')
def delete_profile_parent(request):
    user = request.user
    print(user)
    if request.method == "POST":
        user.delete()
        messages.info(request, 'Your account deleted successfully')
        return redirect('mainpage')
    return render(request,'delete_account_parent.html')


