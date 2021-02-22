from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('contact', views.contact),
    path('home', article_views.article_list, name = "articles"),
    path('', views.home, name = "home"),
    path('all-articles/', article_views.all_articles, name = "all_articles"),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
