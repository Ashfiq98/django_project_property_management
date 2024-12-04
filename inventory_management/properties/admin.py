from django.contrib.auth.admin import UserAdmin
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Location, Accommodation, LocalizeAccommodation
from django.contrib.auth.models import User


# Create a resource class for the Location model
class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        fields = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city', 'created_at', 'updated_at')


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin, LeafletGeoAdmin):
    list_display = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'state_abbr', 'city', 'location_type')
    list_filter = ('location_type', 'country_code', 'state_abbr')

    # Enable the import/export functionality
    resource_class = LocationResource


@admin.register(Accommodation)
class AccommodationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'published', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'location__title')
    list_filter = ('country_code', 'published', 'review_score')
    autocomplete_fields = ('location', 'user')  # For autocomplete fields

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Disable the 'user' field for staff users
        if request.user.is_staff and not request.user.is_superuser:
            form.base_fields['user'].initial = request.user
            form.base_fields['user'].disabled = True
        return form

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False
        return super().has_view_permission(request, obj)


@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('property', 'language', 'description')
    search_fields = ('property__title', 'language', 'description')
    list_filter = ('language',)


# Enable autocomplete for User model
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields = ('username', 'email', 'first_name', 'last_name')
