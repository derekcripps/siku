from django.contrib import admin
from .models import Album, Artist, Track, Playlist

# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(Playlist)
