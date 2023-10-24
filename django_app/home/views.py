from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    numbers = {
        'num1': [1,2,3,4,5,6,7,8,9]
    }

    return render(request,'index.html', numbers)

def about(request):
    return render(request,'About.html')


def booking(request):
    return render(request,'Booking.html')


def doctor(request):
    return render(request,'Doctors.html')


def contact(request):
    return render(request,'Contact.html')


def department(request):
    return render(request,'Department.html')