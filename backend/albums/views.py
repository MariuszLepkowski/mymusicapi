from albums.models import Album
from albums.serializers import AlbumSerializer
from rest_framework import viewsets


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
