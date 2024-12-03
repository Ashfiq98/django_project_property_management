from django.contrib.auth.admin import UserAdmin
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Location, Accommodation, LocalizeAccommodation
from django.contrib.auth.models import User


@admin.register(Location)
class LocationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'state_abbr', 'city', 'location_type')
    list_filter = ('location_type', 'country_code', 'state_abbr')


@admin.register(Accommodation)
class AccommodationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'published', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'location__title')
    list_filter = ('country_code', 'published', 'review_score')
    autocomplete_fields = ('location', 'user')  # For autocomplete fields

    # Override get_form to restrict the location and user fields
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Filter the location dropdown to show only locations added by the admin
        if not request.user.is_superuser:
            form.base_fields['location'].queryset = Location.objects.all()  # Show all locations to users
        
        # Restrict the user field to show only the logged-in user for regular users
        if not request.user.is_superuser:
            form.base_fields['user'].queryset = User.objects.filter(id=request.user.id)  # Show only the logged-in user for regular users
        
        return form

    # Override get_queryset to limit the displayed accommodations to the logged-in user's properties
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:  # Only allow property owners to see their own accommodations
            queryset = queryset.filter(user=request.user)
        return queryset

    # Restrict actions for non-superusers: they can only change their own accommodations
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False  # Allow changing only own accommodations
        return super().has_change_permission(request, obj)

    # Restrict delete permissions for non-superusers: they can only delete their own accommodations
    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False  # Allow deleting only own accommodations
        return super().has_delete_permission(request, obj)

    # Restrict view permissions for non-superusers: they can only view their own accommodations
    def has_view_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser:
            return False  # Allow viewing only own accommodations
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
