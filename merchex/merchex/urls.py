from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('listing/', views.listing),
    path('contact/', views.contact),
    path('about-us/', views.about_us),
]
