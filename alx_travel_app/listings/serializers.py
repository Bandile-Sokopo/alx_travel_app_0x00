from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Listing
        fields = ["id", "title", "description", "location", "price_per_night", "owner", "created_at"]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    listing = serializers.ReadOnlyField(source="listing.title")

    class Meta:
        model = Booking
        fields = ["id", "user", "listing", "start_date", "end_date", "created_at"]
