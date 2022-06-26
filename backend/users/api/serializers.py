from dataclasses import field
from rest_framework import serializers
from users.models import Profile
from listings.models import Listing
from listings.api.serializers import ListingSerializer

class ProfileSerializer(serializers.ModelSerializer):
    seller_listings = serializers.SerializerMethodField()

    def get_seller_listings(self, obj):
        listings = Listing.objects.filter(seller=obj.seller)
        listings_serialized = ListingSerializer(listings, many=True)
        return listings_serialized.data

    class Meta:
        model = Profile
        fields = '__all__'