import json
from django.core.management.base import BaseCommand
from properties.models import Location


class Command(BaseCommand):
    help = 'Generate a sitemap.json file for all country locations'

    def handle(self, *args, **kwargs):
        # Group locations by country
        countries = {}
        locations = Location.objects.all()

        for location in locations:
            country_code = location.country_code
            if country_code not in countries:
                countries[country_code] = {
                    "name": country_code.upper(),
                    "locations": []
                }
            
            # Generate the slug-based URL pattern
            location_slug = location.title.lower().replace(' ', '-')
            url = f"{country_code.lower()}/{location_slug}"
            countries[country_code]["locations"].append({
                location.title: url
            })

        # Convert countries to a sorted list
        sitemap = []
        for country_code, data in countries.items():
            data["locations"].sort(key=lambda x: list(x.keys())[0])  # Sort by location name
            sitemap.append({
                data["name"]: country_code.lower(),
                "locations": data["locations"]
            })

        # Sort countries alphabetically
        sitemap.sort(key=lambda x: list(x.keys())[0])

        # Save to sitemap.json
        with open('sitemap.json', 'w') as f:
            json.dump(sitemap, f, indent=4)

        self.stdout.write(self.style.SUCCESS('sitemap.json file has been generated successfully!'))
