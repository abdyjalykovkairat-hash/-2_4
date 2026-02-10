from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone')
    