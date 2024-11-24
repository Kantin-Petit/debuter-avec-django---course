from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from listings.models import Listing
from listings.models import Band
from listings.forms import BandForm, ContactUsForm, ListingForm

## Band views
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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance = band)
    return render(request,
                  'listings/band_update.html',
                  {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})

## Listing views
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

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)  
    else:
        form = ListingForm()
    return render(request,
            'listings/listing_create.html',
            {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance = listing)
    return render(request,
                  'listings/listing_update.html',
                  {'form': form})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request,
                  'listings/listing_delete.html',
                  {'listing': listing})

## Contact views
def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "Anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
                )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    
    return render(request, 
                  'listings/contact.html',
                  {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')


## About views
def about_us(request):
    return render(request, 'listings/about_us.html')