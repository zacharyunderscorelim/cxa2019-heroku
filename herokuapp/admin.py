from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from herokuapp.models import Shop


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ("name", "location")

# Register your models here.
from herokuapp.models import Category, Page, UserProfile
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)