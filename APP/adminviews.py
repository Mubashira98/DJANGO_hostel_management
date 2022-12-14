from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from APP.forms import hostel_form, food_form, fee_form, notification_form, attendance_form, staff_form, \
    roombooking_form, complaint_form, reply_form

from APP.models import Student_register, Parent_register, Hostel, Food, Fee, Notification, Attendance, Payment, Review, \
    Staff, Room_booking, Complaint


def viewstudents(request):
    data = Student_register.objects.all()
    return render(request,'viewstudent.html',{'data':data})

def viewsparents(request):
    data = Parent_register.objects.all()
    return render(request,'viewparent.html',{'data':data})

def approve_student(request,id):
    student = Student_register.objects.get(id=id)
    print(student)
    # student.approval_status=True
    student.approval_status = 1
    student.save()
    messages.info(request,'Student approved successfully')
    return redirect('viewstudents')

def reject_student(request,id):
        student = Student_register.objects.get(id=id)
    # if request.method == "POST":
        student.approval_status = 2
        student.save()
        messages.info(request,'Student registration rejected')
        return redirect('viewstudents')
    # return render(request,'viewstudent.html')

def approve_parent(request,id):
    parent = Parent_register.objects.get(id=id)
    print(parent)
    # student.approval_status=True
    parent.approval_status = 1
    parent.save()
    messages.info(request,'parent approved successfully')
    return redirect('viewsparents')

def reject_parent(request, id):
    parent = Parent_register.objects.get(id=id)
    # if request.method == "POST":
    parent.approval_status = 2
    parent.save()
    messages.info(request, 'parent registration rejected')
    return redirect('viewsparents')
    # return render(request,'viewstudent.html')

def add_hostel(request):
    form = hostel_form()
    if request.method == "POST":
        form = hostel_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_hostel')
    return render(request,'add_hostel.html',{'form':form})

def view_hostel(request):
    data = Hostel.objects.all()
    return render(request,'view_hostel_details.html',{'data':data})

def hostel_update(request,id):
    hostel1 = Hostel.objects.get(id=id)
    form = hostel_form(instance=hostel1)
    if request.method == 'POST':
        form = hostel_form(request.POST,request.FILES,instance=hostel1)
        if form.is_valid():
            form.save()
        return redirect('view_hostel')
    return render(request,'update_hostel.html',{'form':form})

def hostel_delete(request,id):
    Hostel.objects.get(id=id).delete()
    return redirect('view_hostel')

def add_food(request):
    form = food_form()
    if request.method == "POST":
        form = food_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    return render(request,'add_food.html',{'form':form})

def view_food(request):
    data = Food.objects.all()
    return render(request, 'view_food_details.html', {'data': data})

def food_update(request,id):
    food1 = Food.objects.get(id=id)
    form = food_form(instance=food1)
    if request.method == 'POST':
        form = food_form(request.POST,instance=food1)
    if form.is_valid():
        form.save()
        return redirect('view_food')
    return render(request,'update_food_details.html',{'form':form})

def food_delete(request,id):
    Food.objects.get(id=id).delete()
    return redirect('view_food')

def add_fee(request):
    form = fee_form()
    if request.method == "POST":
        form = fee_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_fee')
    return render(request,'add_fee.html',{'form':form})

def view_fee(request):
    data = Fee.objects.all()
    return render(request, 'view_fee_details.html', {'data': data})

def fee_update(request,id):
    fee1 = Fee.objects.get(id=id)
    form = fee_form(instance=fee1)
    if request.method == 'POST':
        form = fee_form(request.POST,instance=fee1)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request,'update_fee_details.html',{'form':form})

def fee_delete(request,id):
    Fee.objects.get(id=id).delete()
    return redirect('view_fee')

def add_notification(request):
    form = notification_form()
    if request.method == "POST":
        form = notification_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_notification')
    return render(request,'add_notification.html',{'form':form})

def view_notification(request):
    data = Notification.objects.all()
    return render(request, 'view_notification.html', {'data': data})

def notification_update(request,id):
    not1 = Notification.objects.get(id=id)
    form = notification_form(instance=not1)
    if request.method == 'POST':
        form = notification_form(request.POST,instance=not1)
    if form.is_valid():
        form.save()
        return redirect('view_notification')
    return render(request,'update_notification.html',{'form':form})

def notification_delete(request,id):
    Notification.objects.get(id=id).delete()
    return redirect('view_notification')

def add_attendance(request):
    form = attendance_form()
    if request.method == "POST":
        form = attendance_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request,'add_attendance.html',{'form':form})

def view_attendance(request):
    data = Attendance.objects.all()
    return render(request, 'view_attendance_details.html', {'data': data})

def attendance_update(request,id):
    att1 = Attendance.objects.get(id=id)
    form = attendance_form(instance=att1)
    if request.method == 'POST':
        form = attendance_form(request.POST,instance=att1)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request,'update_attendance.html',{'form':form})

def attendance_delete(request,id):
    Attendance.objects.get(id=id).delete()
    return redirect('view_attendance')

def payment_view(request):
    data = Payment.objects.all()
    return render(request, 'view_payment_details.html', {'data': data})


def view_review_details(request):
    data = Review.objects.all()
    return render(request,'view_review_details.html',{'data':data})

def add_staff(request):
    form = staff_form()
    if request.method == "POST":
        form = staff_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request,'add_staff.html',{'form':form})

def view_staff(request):
    data = Staff.objects.all()
    return render(request, 'view_staff_details.html', {'data': data})

def staff_update(request,id):
    staff1 = Staff.objects.get(id=id)
    form = staff_form(instance=staff1)
    if request.method == 'POST':
        form = staff_form(request.POST,instance=staff1)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'update_staff.html',{'form':form})

def staff_delete(request,id):
    Staff.objects.get(id=id).delete()
    return redirect('view_staff')

def admin_view_room_booking(request):
    data = Room_booking.objects.all()
    return render(request, 'admin_view_roombooking.html', {'data': data})

def approve_roombooking(request,id):
    booking1 = Room_booking.objects.get(id=id)
    # student.approval_status=True
    booking1.booking_status = 1
    booking1.save()
    messages.info(request,'roombooking approved successfully')
    return redirect('admin_view_room_booking')

def reject_roombooking(request,id):
        booking1 = Room_booking.objects.get(id=id)
    # if request.method == "POST":
        booking1.booking_status = 2
        booking1.save()
        messages.info(request,'room booking rejected')
        return redirect('admin_view_room_booking')

def admin_view_complaint(request):
    data = Complaint.objects.all()
    return render(request, 'admin_view_complaint.html', {'data': data})

def admin_reply(request,id):
    reply1 = Complaint.objects.get(id=id)
    form = reply_form(instance=reply1)
    if request.method == 'POST':
        form = reply_form(request.POST,instance=reply1)
    if form.is_valid():
        form.save()
        return redirect('admin_view_complaint')
    return render(request,'admin_complaint_reply.html',{'form':form})








