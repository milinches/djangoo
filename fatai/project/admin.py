from django.contrib import admin
from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender', 'receiver', 'signed_for_by', 'date', 'time')
    list_filter = ('status',)
    search_fields = ('tracking_number',)

# Register your models here.

admin.site.register(Track, TrackAdmin)