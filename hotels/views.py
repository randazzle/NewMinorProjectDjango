from django.shortcuts import render
from .models import Hotel
# from django.contrib.gis.geoip2 import GeoIP2

mapbox_access_token = 'pk.eyJ1IjoicmFuZGF6emxlIiwiYSI6ImNrbG5uM2t2aDAwY2IybnA2bGN1YWF0N3QifQ.r1nyniJdTbVwWclWGc3tWw'



# Create your views here.
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotels_list.html', context={'hotels':hotels, 'mapbox_access_token': mapbox_access_token})

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(slug=slug)
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
    return render(request, 'hotels/hotel_detail.html', context={'hotel':hotel, 'mapbox_access_token': mapbox_access_token})