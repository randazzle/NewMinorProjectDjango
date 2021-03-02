from django.shortcuts import render
from .models import Hotel
from geopy.distance import geodesic
# from django.contrib.gis.geoip2 import GeoIP2

mapbox_access_token = 'pk.eyJ1IjoicmFuZGF6emxlIiwiYSI6ImNrbG5uM2t2aDAwY2IybnA2bGN1YWF0N3QifQ.r1nyniJdTbVwWclWGc3tWw'

#Utilities
def calculate_center(lat1,lon1,lat2,lon2):
    lat_center = (lat1 + lat2)/2
    lon_center = (lon1 + lon2)/2
    return lat_center, lon_center

# Create your views here.
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotels_list.html', context={'hotels':hotels, 'mapbox_access_token': mapbox_access_token})

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(slug=slug)
    lat = request.POST.get('lat', 27.699406964053935)
    lon = request.POST.get('lon', 85.2971295682943)
    # print("LAT=", lat, "LONG=",lon)
    # print("HOTEL LAT=", hotel.latitude, "HOTEL LONG=", hotel.longitude)

    user_location = (lat, lon)
    hotel_location = (hotel.latitude, hotel.longitude)
    # print("Distance in KM",geodesic(user_location, hotel_location).km)

    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')

    # print("IP ADDRESS:",ip)
    # g = GeoIP2()
    # lat, lon = g.lat_lon(ip)
    # print("Latitude = ", lat , "Longitude=", lon)
    # g = GeoIP() 
    # lat,lng = g.lat_lon(user_ip)

    lat_center, lon_center = calculate_center(lat, lon, hotel.latitude, hotel.longitude)
    return render(request, 'hotels/hotel_detail.html', context={'hotel':hotel, 'mapbox_access_token': mapbox_access_token, 'lat_center': lat_center, 'lon_center': lon_center})

def hotels_nearby(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotels_nearby_get.html', context={'hotels':hotels, 'mapbox_access_token': mapbox_access_token})