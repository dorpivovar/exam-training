from django.contrib import admin
from .models import Events
# Register your models here.

@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'event_date', 'max_guests', 'created_at')
    search_fields = ('title', 'location')
    