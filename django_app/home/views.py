from django.shortcuts import render
from django.http import HttpResponse
from . models import Departments, Doctors
from . forms import BookingForm
# Create your views here.
def index(request):

    numbers = {
        'num1': [1,2,3,4,5,6,7,8,9]
    }

    return render(request,'index.html', numbers)

def about(request):
    return render(request,'About.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'Booking.html', dict_form)


def doctor(request):
    dict_doctors = {
        'doc': Doctors.objects.all()
    }
    return render(request,'Doctors.html', dict_doctors)


def contact(request):
    return render(request,'Contact.html')


def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request,'Department.html', dict_dept)