from django.shortcuts import render,redirect
from app1.models import Student
from django.core.paginator import Paginator


# Create your views here.

def creates(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        pincode = request.POST['pincode']
        email = request.POST['email']

        s = Student(fname = fname, lname = lname, address= address, pincode = pincode, email = email)
        s.save()
        return redirect("lists")

    return render(request,'create.html')

def lists(request):
    s_list = Student.objects.all().order_by('-id')
    paginator = Paginator(s_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'list.html',{'page_obj':page_obj})


def deletes(request,pk):
    s_detail = Student.objects.get(id=pk)
    s_detail.delete()
    return redirect('lists')

def edits(request,pk):
    s_edit = Student.objects.get(id=pk)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        pincode = request.POST['pincode']
        email = request.POST['email']

        s_edit.fname = fname
        s_edit.lname = lname
        s_edit.address = address
        s_edit.pincode = pincode
        s_edit.email = email

        s_edit.save()

        return redirect("lists")


    return render(request,'update.html',{'s_edit':s_edit})

def details(request,pk):
    d_student = Student.objects.filter(id=pk)[0]

    return render(request,'detail.html',{"s_detail":d_student})