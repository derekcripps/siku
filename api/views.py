from siku.models import Artist, Album
from rest_framework import viewsets
from api.serializers import AlbumSerializer, ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

