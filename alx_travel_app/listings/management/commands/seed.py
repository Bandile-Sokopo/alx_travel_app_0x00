from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        # Ensure at least one user exists
        user, created = User.objects.get_or_create(username="demo_user", defaults={"password": "password123"})

        sample_listings = [
            {
                "title": "Cozy Apartment in Cape Town",
                "description": "A lovely apartment with sea views.",
                "location": "Cape Town",
                "price_per_night": 750.00,
            },
            {
                "title": "Modern Loft in Johannesburg",
                "description": "Spacious loft perfect for city travelers.",
                "location": "Johannesburg",
                "price_per_night": 950.00,
            },
            {
                "title": "Beach House in Durban",
                "description": "Relax by the ocean in this beachfront house.",
                "location": "Durban",
                "price_per_night": 1200.00,
            },
        ]

        for listing_data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=listing_data["title"],
                defaults={**listing_data, "owner": user}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
