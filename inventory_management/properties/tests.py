from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from properties.models import Location, Accommodation, LocalizeAccommodation


class LocationModelTest(TestCase):
    def setUp(self):
        # Create a sample location for testing
        self.location = Location.objects.create(
            id='test_location_1',
            title='Test Location',
            location_type='city',
            country_code='US',
            state_abbr='CA',
            city='San Francisco',
            center=Point(-122.4194, 37.7749)
        )

    def test_location_creation(self):
        """Test Location model creation"""
        self.assertTrue(isinstance(self.location, Location))
        self.assertEqual(self.location.__str__(), 'Test Location (San Francisco, US)')
        self.assertEqual(self.location.country_code, 'US')
        self.assertEqual(self.location.state_abbr, 'CA')

    def test_location_fields(self):
        """Test Location model fields"""
        self.assertIsNotNone(self.location.created_at)
        self.assertIsNotNone(self.location.updated_at)


class AccommodationModelTest(TestCase):
    def setUp(self):
        # Create a user and location first
        self.user = User.objects.create_user(
            username='testuser', 
            password='12345'
        )
        
        # Create a location
        self.location = Location.objects.create(
            id='test_location_1',
            title='Test Location',
            country_code='US',
            state_abbr='CA',
            city='San Francisco'
        )

        # Create an accommodation
        self.accommodation = Accommodation.objects.create(
            id='test_accommodation_1',
            title='Test Accommodation',
            country_code='US',
            bedroom_count=2,
            review_score=4.5,
            usd_rate=100.00,
            center=Point(-122.4194, 37.7749),
            images={'main': 'test_image.jpg'},
            location=self.location,
            amenities={'wifi': True, 'kitchen': True},
            user=self.user,
            published=True
        )

    def test_accommodation_creation(self):
        """Test Accommodation model creation"""
        self.assertTrue(isinstance(self.accommodation, Accommodation))
        self.assertEqual(self.accommodation.title, 'Test Accommodation')
        self.assertEqual(self.accommodation.bedroom_count, 2)
        self.assertEqual(self.accommodation.review_score, 4.5)

    def test_accommodation_relationships(self):
        """Test relationships between models"""
        self.assertEqual(self.accommodation.location, self.location)
        self.assertEqual(self.accommodation.user, self.user)


class LocalizeAccommodationModelTest(TestCase):
    def setUp(self):
        # Create dependencies first
        self.user = User.objects.create_user(
            username='testuser', 
            password='12345'
        )
        
        self.location = Location.objects.create(
            id='test_location_1',
            title='Test Location',
            country_code='US',
            state_abbr='CA',
            city='San Francisco'
        )

        self.accommodation = Accommodation.objects.create(
            id='test_accommodation_1',
            title='Test Accommodation',
            country_code='US',
            bedroom_count=2,
            review_score=4.5,
            usd_rate=100.00,
            center=Point(-122.4194, 37.7749),
            images={'main': 'test_image.jpg'},
            location=self.location,
            amenities={'wifi': True, 'kitchen': True},
            user=self.user,
            published=True
        )

        # Create a localized accommodation
        self.localize = LocalizeAccommodation.objects.create(
            property=self.accommodation,
            language='es',
            description='Descripción de prueba',
            policy={'cancelation': 'Flexible'}
        )

    def test_localize_accommodation_creation(self):
        """Test LocalizeAccommodation model creation"""
        self.assertTrue(isinstance(self.localize, LocalizeAccommodation))
        self.assertEqual(self.localize.language, 'es')
        self.assertEqual(self.localize.property, self.accommodation)