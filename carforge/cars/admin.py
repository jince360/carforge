from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ("car_type",)
    search_fields = ("car_type",)
    list_filter = ("car_type",)

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ("fuel",)
    search_fields = ("fuel",)
    list_filter = ("fuel",)

@admin.register(Condition)
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

@admin.register(Transmission)
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
    list_display = ("brand", "model", "year", "price", "state", "is_featured")
    search_fields = ("brand__name", "model", "identification_number")
    list_filter = ("brand", "fuel", "transmission", "condition", "state", "year")
    inlines = [AdditionalImagesInline]  
