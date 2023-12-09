from django.shortcuts import render
from.models import StudentModels
from.forms import Studentform

def index(request):
    rg=Studentform
    return render(request,"index.html",{"forms":rg})


def display(request):
    eg=StudentModels.objects.all()
    return render(request,"display.html",{"data":eg})


def saved(request):
    idno=request.POST.get("n1")
    fname=request.POST.get("n2")
    lname=request.POST.get("n3")
    age=request.POST.get("n4")
    email=request.POST.get("n5")
    fd=StudentModels(idno=idno,fname=fname,lname=lname,age=age,email=email)
    fd.save()
    msg="Data are saved successfully"
    return render(request,"index.html",{"message":msg})