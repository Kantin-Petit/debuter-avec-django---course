from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/update/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),

    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/add/', views.listing_create, name='listing-create'),
    path('listings/<int:id>/update/', views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing-delete'),

    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about'),

    path('email-sent/', views.email_sent, name='email-sent'),
]
