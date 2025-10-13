from albums.models import Album
from albums.serializers import AlbumSerializer
from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed, created, updated and deleted.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
