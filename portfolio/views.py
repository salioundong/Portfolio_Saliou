from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def projectA(request):
    return render(request, "portfolio/projectA.html")