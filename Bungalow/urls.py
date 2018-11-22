"""Bungalow URL Configuration
"""
from django.conf.urls import url, include
from rest_framework import routers
from Bungalow.Rental_API import views

router = routers.DefaultRouter()
router.register(r'listings', views.ListingViewSet)

# Wire up API using automatic URL routing.
urlpatterns = [
    url(r'^api/', include(router.urls)),
]
