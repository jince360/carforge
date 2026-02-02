from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")