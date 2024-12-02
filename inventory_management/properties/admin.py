from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location, Accommodation, LocalizeAccommodation


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'state_abbr', 'city', 'location_type')
    list_filter = ('location_type', 'country_code', 'state_abbr')


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'published', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'location__title')
    list_filter = ('country_code', 'published', 'review_score')
    raw_id_fields = ('location',)
    autocomplete_fields = ('user',)


@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('property', 'language', 'description')
    search_fields = ('property__title', 'language', 'description')
    list_filter = ('language',)
