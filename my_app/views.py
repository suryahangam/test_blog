from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience


def home(request):
    experience = Experience.objects.all()

    return render(request, 'index.html', {'experience': experience})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return HttpResponse("blog")

def portfolio(request):
    return HttpResponse("portfolio")

def contact(request):
    return HttpResponse("contact")
