from django.urls import path, re_path
from .import views

app_name = 'hotels'

urlpatterns = [
    path('hotels_list/', views.hotel_list, name = "hotels_list"),
    path('hotels_nearby/', views.hotels_nearby, name = "hotels_nearby"),
    re_path('hotel_detail/(?P<slug>[\w-]+)/$', views.hotel_detail, name = "hotel_detail"),
]
