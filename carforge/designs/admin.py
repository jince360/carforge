from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40' height='40' style='object-fit: cover; border-radius: 10px;' />", object.image.url)
    thumbnail.short_description = "Photo"
    list_display = ("id", "thumbnail","title", "is_active")
    list_display_links = ("title", "thumbnail",)
    search_fields = ("title",)
    list_filter = ("is_active",)