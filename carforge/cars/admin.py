from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ("car_type",)
    search_fields = ("car_type",)
    list_filter = ("car_type",)


class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ("fuel",)
    search_fields = ("fuel",)
    list_filter = ("fuel",)


class ConditionAdmin(admin.ModelAdmin):
    list_display = ("condition",)
    search_fields = ("condition",)
    list_filter = ("condition",)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "hexcode",)
    search_fields = ("name", "hexcode",)
    list_filter = ("name", "hexcode",)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


class TransmissionAdmin(admin.ModelAdmin):
    list_display = ("transmission",)
    search_fields = ("transmission",)
    list_filter = ("transmission",)

class AdditionalImagesInline(admin.TabularInline):

    model = AdditionalImages
    extra = 1
    fields = ("image",)
    readonly_fields = ()

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}  

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40' height='40' style='object-fit: cover; border-radius: 10px;' />", object.featured_image.url)
    thumbnail.short_description = "Photo"
    list_display = ("thumbnail","brand", "model", "year", "price", "state", "is_featured", "color", "is_available","is_active")
    list_editable = ("is_featured", "is_available", "is_active")
    list_display_links = ("thumbnail", "brand")
    search_fields = ("brand__name", "model", "identification_number", "color__name", "state", "city", "type__car_type",)
    list_filter = ("brand", "fuel", "transmission", "condition", "state", "year")
    inlines = [AdditionalImagesInline]  
    filter_horizontal = ("car_features",) 
