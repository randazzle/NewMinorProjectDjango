from django.urls import path, re_path
from .import views
from TourismAid import views as main_views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name = "list"),
    re_path('(?P<slug>[\w-]+)/$', views.article_detail, name = "detail"),
    path('about/', main_views.about, name = "about"),
    path('contact/', main_views.contact, name = "contact"),
]
