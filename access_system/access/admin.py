from django.contrib import admin
from .models import AccessEntry

@admin.register(AccessEntry)
class AccessEntryAdmin(admin.ModelAdmin):
    list_display = ('uid', 'phone', 'email', 'access_start', 'access_duration', 'created_at')
    fields = ('uid', 'phone', 'email', 'access_start', 'access_duration')
