from django.contrib import admin

from listings.models import Band
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')
admin.site.register(Band, BandAdmin)

from listings.models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'year', 'sold')
admin.site.register(Listing, ListingAdmin)