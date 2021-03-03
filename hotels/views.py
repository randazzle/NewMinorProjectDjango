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

def calculate_zoom(distance):
    if (distance<1):
        return 14
    elif (distance>=1 and distance<4):
        return 13.5
    elif (distance>=4 and distance<10):
        return 13
    else:
        return 12

# Create your views here.
def hotel_list(request):
    hotels = Hotel.objects.all().order_by('-date')
    return render(request, 'hotels/hotels_list.html', context={'hotels':hotels, 'mapbox_access_token': mapbox_access_token})

def hotels_nearby(request):
    hotels = Hotel.objects.all()[0:6]
    user_lat = request.POST.get('lat', 27.699406964053935)
    user_lon = request.POST.get('lon', 85.2971295682943)
    # print("LOngitude = ", user_lon, "LAtitude = ", user_lat)

    def get_hotel_from_index(index):
            return hotels[index]

    hotel_distances = [None] * len(hotels)
    i=0
    for hotel in hotels:
        hotel_distances[i] = round(geodesic((user_lat, user_lon),(hotel.latitude, hotel.longitude)).km, 5)
        i=i+1
        # print(i,"=",hotel_distances[i])

    nearest_hotels = list(enumerate(hotel_distances))
    # print("Nearest Hotels List = ",nearest_hotels)

    sorted_nearest_hotels= sorted(nearest_hotels, key = lambda x : x[1])
    # print("Sorted Nearest Hotels = ", sorted_nearest_hotels)

    nearby_hotels = [None] * 5
    p = 0
    for each in sorted_nearest_hotels:
        # print("Hotel: ", get_hotel_from_index(each[0]))
        nearby_hotels[p] = get_hotel_from_index(each[0])
        p = p + 1
        if(p>4):
            break

    return render(request, 'hotels/hotels_nearby.html', context={'hotels':nearby_hotels, 'mapbox_access_token': mapbox_access_token})

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
    distance = round(geodesic((lat, lon),(hotel.latitude, hotel.longitude)).km, 5)
    zoomm = calculate_zoom(distance)
    print("ZOOM = ",zoomm)
    return render(request, 'hotels/hotel_detail.html', context={'hotel':hotel, 'mapbox_access_token': mapbox_access_token, 'lat_center': lat_center, 'lon_center': lon_center, 'zoomm':zoomm})

