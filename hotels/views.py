from django.shortcuts import render
from .models import Hotel


mapbox_access_token = 'pk.eyJ1IjoicmFuZGF6emxlIiwiYSI6ImNrbG5uM2t2aDAwY2IybnA2bGN1YWF0N3QifQ.r1nyniJdTbVwWclWGc3tWw'

# Create your views here.
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotels_list.html', context={'hotels':hotels, 'mapbox_access_token': mapbox_access_token})

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(slug=slug)
    return render(request, 'hotels/hotel_detail.html', context={'hotel':hotel, 'mapbox_access_token': mapbox_access_token})