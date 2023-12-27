from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing
from listings.models import Band

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/band_list.html', 
                  {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 
                  'listings/band_detail.html', 
                  {'band': band})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 
                  'listings/listing_list.html', 
                  {'listings': listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 
                  'listings/listing_detail.html', 
                  {'listing': listing})

def contact(request):
    return render(request, 'listings/contact.html')

def about_us(request):
    return render(request, 'listings/about_us.html')