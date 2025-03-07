from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def soccer2023(request):
    return render(request, "portfolio/soccer_2023.html")

def roboGenius(request):
    return render(request, "portfolio/RoboGenius.html")

def materialManage(request):
    return render(request, "portfolio/materialManage.html")

def meteo(request):
    return render(request, "portfolio/meteo.html")