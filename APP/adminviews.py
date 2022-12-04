from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from APP.forms import hostel_form
from APP.models import Student_register, Parent_register, Hostel


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
            return redirect('admin1')
    return render(request,'add_hostel.html',{'form':form})

def view_hostel(request):
    data = Hostel.objects.all()
    return render(request,'view_hostel_details.html',{'data':data})

def hostel_update(request,id):
    hostel1 = Hostel.objects.get(id=id)
    form = hostel_form(instance=hostel1)
    if request.method == 'POST':
        form = hostel_form(request.POST,instance=hostel1)
    if form.is_valid():
        form.save()
        return redirect('view_hostel')
    return render('view_hostel_details.html',{'form':form})

def hostel_delete(request,id):
    Hostel.objects.get(id=id).delete()
    return redirect('view_hostel')