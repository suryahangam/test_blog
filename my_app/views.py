from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    name = "hello"
    age = 10
    return HttpResponse("This is my home")
