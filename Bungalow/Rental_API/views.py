from django.shortcuts import render
from rest_framework import viewsets
from Bungalow.Rental_API.serializers import ListingSerializer
from Bungalow.Rental_API.models import Listing
from django_filters.rest_framework import DjangoFilterBackend



class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('area_unit','bathrooms','bedrooms','home_size','home_type','last_sold_date','last_sold_price','link','price','property_size','rent_price','rentzestimate_amount','rentzestimate_last_updated','tax_value','tax_year','year_built','zestimate_amount','zestimate_last_updated','zillow_id','address','city','state','zipcode')
