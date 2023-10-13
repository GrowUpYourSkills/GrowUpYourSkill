from django.shortcuts import render , HttpResponse
from home.models import Contact, Registration
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method =="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        message = request.POST.get('message')
        contact =  Contact(firstname=firstname, lastname=lastname, email=email, 
        country=country,message=message, gender=gender, age=age, date=datetime.today())
        contact.save()

    return render(request, "contact.html")


def pyton(request):
    return render(request, "pyton.html")

def jango(request):
    return render(request, "jango.html")

def jango(request):
    return render(request, "janngo.html")

def front(request):
    return render(request, "front.html")

def javas(request):
    return render(request, "javas.html")

def csss(request):
    return render(request, "csss.html")

def cpplus(request):
    return render(request, "cpplus.html")

def registration(request):
    if request.method == "POST":
        firstname = request.POST.get ('firstname')
        lastname = request.POST.get ('lastname')
        email = request.POST.get ('email')
        country = request.POST.get ('country')
        course = request.POST.get ('course')
        gender = request.POST.get ('gender')
        age = request.POST.get ('age')
        payment_method = request.POST.get ('payment_method')
        registration = Registration(firstname=firstname, lastname=lastname, email=email, country=country,
        course=course ,gender=gender, age=age, payment_method=payment_method, date=datetime.today())

        registration.save()


    return render(request, "registration.html")
