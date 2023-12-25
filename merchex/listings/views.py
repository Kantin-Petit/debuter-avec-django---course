from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def about_us(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")