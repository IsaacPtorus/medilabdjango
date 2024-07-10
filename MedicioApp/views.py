from django.shortcuts import render, redirect
from MedicioApp.models import Contact, Appointment, Branch


# Create your views here.
def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'docs.html')


def contact(request):
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message'])
        all.save()
        return redirect('contact/')
    else:
        return render(request, 'contact.html')
    # the above takes us to the next page.to remain in the same page or go to another,enter tghe url of the page.the one ive put above takes me to home page coz my url for index(home page) is empty
    # return render(request, 'contact.html')


def appointment(request):
    if request.method == 'POST':
        app = Appointment(name=request.POST['name'],
                          email=request.POST['email'],
                          phone=request.POST['phone'],
                          message=request.POST['message'],
                          doctor=request.POST['doctor'],
                          date=request.POST['date'],
                          department=request.POST['department']
                          )
        app.save()
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')


#
def branch(request):
    if request.method == 'POST':
        b2 = Branch(name=request.POST['name'],
                    email=request.POST['email'],
                    manager=request.POST['manager'],
                    location=request.POST['location'])
        b2.save()
        return redirect('branch/')
    else:
        return render(request, 'branch.html')
