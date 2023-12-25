from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello.html', 
                  {'bands': bands})

def listing(request):
    listings = Listing.objects.all()
    return render(request, 
                  'listings/listing.html', 
                  {'listings': listings})

def contact(request):
    return render(request, 'listings/contact.html')

def about_us(request):
    return render(request, 'listings/about_us.html')