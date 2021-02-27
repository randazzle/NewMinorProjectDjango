from django.contrib import admin
from .models import Hotel

# Register your models here.
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Hotel, HotelAdmin)