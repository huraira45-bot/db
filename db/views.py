from django.http import HttpResponse
from service.models import Service
from django.shortcuts import render

def home(request):
    return render(request, "Home.html")


def ab(request):
    return render(request, "About.html")

def mp(request):
    return render(request, "Mp3.html")

def se(request):
    return render(request,"Security.html") 

def img(request):
    return render(request,"Img.html")           








def db(request):
    serviceData=Service.objects.all()
    for n in serviceData:
        print(n.service_icon)
   
    data={
        'serviceData':serviceData
    }

    return render(request,"index.html",data)