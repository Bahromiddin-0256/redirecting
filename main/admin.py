from django.contrib import admin

from main.models import Settings


# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('use_example_link', 'example_link')
