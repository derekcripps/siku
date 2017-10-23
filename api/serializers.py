from siku.models import Album, Artist, Track
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'release_date', 'rating', 'image')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('name', )

