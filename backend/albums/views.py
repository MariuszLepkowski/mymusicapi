import random

from albums.models import Album
from albums.pagination import CustomPagination
from albums.serializers import AlbumSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import AlbumFilter


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed, created, updated and deleted.
    """

    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = AlbumFilter
    filterset_fields = ["artist", "title", "year", "genre"]
    search_fields = ["artist", "title", "year", "genre"]
    ordering_fields = ["year", "artist", "title"]
    ordering = ["id"]

    @action(detail=False, methods=["get"])
    def random(self, request):
        count = Album.objects.count()
        if count == 0:
            return Response({"error": "No albums found"}, status=404)

        random_index = random.randint(0, count - 1)
        album = Album.objects.all()[random_index]
        serializer = self.get_serializer(album)
        return Response(serializer.data)
