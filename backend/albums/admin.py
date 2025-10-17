from django.contrib import admin

from .models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "artist", "title", "year", "genre")
    list_display_links = ("id", "title")
    search_fields = ("artist", "title", "genre")
    list_filter = ("year", "genre")
    ordering = ("year", "artist")
