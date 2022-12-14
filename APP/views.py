from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from APP.forms import userregister, StudentForm, Parentform, complaint_form, payment_form, \
    review_form, roombooking_form
from APP.models import Hostel, Food, Complaint, Fee, Payment, Notification, Attendance, Review, Staff, Room_booking, \
    Student_register


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

def student_view_hostel(request):
    data = Hostel.objects.all()
    return render(request,'hostel_view.html',{'data':data})

def student_view_food(request):
    data = Food.objects.all()
    return render(request, 'food_view.html', {'data': data})



def add_complaint(request):
    form = complaint_form()
    if request.method == "POST":
        form = complaint_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_complaint')
    return render(request,'add_a_complaint.html',{'form':form})

def view_complaint(request):
    data = Complaint.objects.all()
    return render(request,'view_complaint.html',{'data':data})

def complaint_update(request,id):
    comp1 = Complaint.objects.get(id=id)
    form = complaint_form(instance=comp1)
    if request.method == 'POST':
        form = complaint_form(request.POST,instance=comp1)
        if form.is_valid():
            form.save()
        return redirect('view_complaint')
    return render(request,'update_complaint.html',{'form':form})

def complaint_delete(request,id):
    Complaint.objects.get(id=id).delete()
    return redirect('view_complaint')

def fee_view(request):
    data = Fee.objects.all()
    return render(request,'fee_view_details.html',{'data':data})

def add_payment(request):
    form = payment_form()
    if request.method == "POST":
        form = payment_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_payment')
    return render(request,'add_payment_details.html',{'form':form})

def view_payment(request):
    data = Payment.objects.all()
    return render(request,'view_payment.html',{'data':data})

def update_payment(request,id):
    pym1 = Payment.objects.get(id=id)
    form = payment_form(instance=pym1)
    if request.method == 'POST':
        form = payment_form(request.POST,instance=pym1)
        if form.is_valid():
            form.save()
        return redirect('view_payment')
    return render(request,'update_payment_details.html',{'form':form})

def delete_payment(request,id):
    Payment.objects.get(id=id).delete()
    return redirect('view_payment')

def notification_view(request):
    data = Notification.objects.all()
    return render(request, 'view_notification_details.html', {'data': data})

def attendance_view(request):
    data = Attendance.objects.all()
    return render(request, 'view_attendance.html', {'data': data})

def add_review(request):
    form = review_form()
    if request.method == "POST":
        form = review_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_review')
    return render(request,'add_review.html',{'form':form})

def view_review(request):
    data = Review.objects.all()
    return render(request,'view_review.html',{'data':data})

def update_review(request,id):
    rev1 = Review.objects.get(id=id)
    form = review_form(instance=rev1)
    if request.method == 'POST':
        form = review_form(request.POST,instance=rev1)
        if form.is_valid():
            form.save()
        return redirect('view_review')
    return render(request,'update_review_details.html',{'form':form})

def delete_review(request,id):
    Review.objects.get(id=id).delete()
    return redirect('view_review')

def student_view_staff(request):
    data = Staff.objects.all()
    return render(request, 'student_view_staff.html', {'data': data})

def add_book_room(request):
    form = roombooking_form()
    if request.method == "POST":
        form = roombooking_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_room_booking')
    return render(request, 'book_room.html', {'form': form})


def view_room_booking(request):
    data = Room_booking.objects.all()
    return render(request, 'student_book_room.html', {'data': data})

def update_roombooking(request,id):
    room1 = Room_booking.objects.get(id=id)
    form = roombooking_form(instance=room1)
    if request.method == 'POST':
        form = roombooking_form(request.POST,instance=room1)
        if form.is_valid():
            form.save()
        return redirect('view_room_booking')
    return render(request,'update_roombooking.html',{'form':form})

def delete_roombooking(request,id):
    Room_booking.objects.get(id=id).delete()
    return redirect('view_room_booking')

def student_viewstudents(request):
    data = Student_register.objects.all()
    return render(request,'student_view_student.html',{'data':data})

# parent views
def parent_view_hostel(request):
    data = Hostel.objects.all()
    return render(request,'parent_hostel_view.html',{'data':data})

def parent_view_staff(request):
    data = Staff.objects.all()
    return render(request, 'parent_view_staff.html', {'data': data})

def parent_attendance_view(request):
    data = Attendance.objects.all()
    return render(request, 'parent_view_attendance.html', {'data': data})

def parent_add_payment(request):
    form = payment_form()
    if request.method == "POST":
        form = payment_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parent_view_payment')
    return render(request,'parent_add_payment_details.html',{'form':form})

def parent_view_payment(request):
    data = Payment.objects.all()
    return render(request,'parent_view_payment.html',{'data':data})

def parent_view_fee(request):
    data = Fee.objects.all()
    return render(request, 'parent_view_fee_details.html', {'data': data})





