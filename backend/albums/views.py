import random

from albums.models import Album
from albums.pagination import CustomPagination
from albums.serializers import AlbumSerializer
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import AlbumFilter


@extend_schema_view(
    list=extend_schema(
        summary="List all albums",
        description=(
            "Retrieve a paginated list of all albums in the database. "
            "Supports filtering, searching, and ordering by artist, title, year, and genre."
        ),
        parameters=[
            OpenApiParameter(
                name="artist",
                description="Filter by artist name",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="title",
                description="Filter by album title",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="year",
                description="Filter by release year",
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name="genre",
                description="Filter by genre",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="search",
                description="Search term across artist, title, year, and genre",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="ordering",
                description="Order results by one or more fields (e.g. `year`, `-artist`)",
                required=False,
                type=str,
            ),
        ],
        responses={
            200: AlbumSerializer(many=True),
        },
        examples=[
            OpenApiExample(
                "List albums response",
                value=[
                    {
                        "id": 1,
                        "artist": "Pink Floyd",
                        "title": "The Dark Side of the Moon",
                        "year": 1973,
                        "genre": "Progressive Rock",
                    },
                    {
                        "id": 2,
                        "artist": "Radiohead",
                        "title": "OK Computer",
                        "year": 1997,
                        "genre": "Alternative Rock",
                    },
                ],
                response_only=True,
            ),
        ],
    ),
    retrieve=extend_schema(
        summary="Retrieve album details",
        description="Get detailed information about a specific album by its ID.",
        responses={
            200: AlbumSerializer,
            404: OpenApiResponse(description="Album not found"),
        },
        examples=[
            OpenApiExample(
                "Retrieve album response",
                value={
                    "id": 1,
                    "artist": "Pink Floyd",
                    "title": "The Dark Side of the Moon",
                    "year": 1973,
                    "genre": "Progressive Rock",
                },
                response_only=True,
            ),
        ],
    ),
    create=extend_schema(
        summary="Create a new album",
        description="Add a new album to the database by providing artist, title, year, and genre.",
        responses={
            201: AlbumSerializer,
            400: OpenApiResponse(description="Invalid input data"),
        },
        examples=[
            OpenApiExample(
                "Create album request",
                value={
                    "artist": "Daft Punk",
                    "title": "Random Access Memories",
                    "year": 2013,
                    "genre": "Electronic",
                },
                request_only=True,
            ),
            OpenApiExample(
                "Create album response",
                value={
                    "id": 3,
                    "artist": "Daft Punk",
                    "title": "Random Access Memories",
                    "year": 2013,
                    "genre": "Electronic",
                },
                response_only=True,
            ),
        ],
    ),
    update=extend_schema(
        summary="Update an album",
        description="Completely update an existing album (all fields required).",
        responses={
            200: AlbumSerializer,
            400: OpenApiResponse(description="Invalid input data"),
            404: OpenApiResponse(description="Album not found"),
        },
        examples=[
            OpenApiExample(
                "Update album request",
                value={
                    "artist": "Pink Floyd",
                    "title": "Wish You Were Here",
                    "year": 1975,
                    "genre": "Progressive Rock",
                },
                request_only=True,
            ),
            OpenApiExample(
                "Update album response",
                value={
                    "id": 1,
                    "artist": "Pink Floyd",
                    "title": "Wish You Were Here",
                    "year": 1975,
                    "genre": "Progressive Rock",
                },
                response_only=True,
            ),
        ],
    ),
    partial_update=extend_schema(
        summary="Partially update an album",
        description="Update one or more fields of an existing album.",
        responses={
            200: AlbumSerializer,
            400: OpenApiResponse(description="Invalid input data"),
            404: OpenApiResponse(description="Album not found"),
        },
        examples=[
            OpenApiExample(
                "Partial update request",
                value={"genre": "Rock"},
                request_only=True,
            ),
            OpenApiExample(
                "Partial update response",
                value={
                    "id": 1,
                    "artist": "Pink Floyd",
                    "title": "The Dark Side of the Moon",
                    "year": 1973,
                    "genre": "Rock",
                },
                response_only=True,
            ),
        ],
    ),
    destroy=extend_schema(
        summary="Delete an album",
        description="Remove an album from the database by its ID.",
        responses={
            204: OpenApiResponse(description="Album deleted successfully"),
            404: OpenApiResponse(description="Album not found"),
        },
    ),
)
class AlbumViewSet(viewsets.ModelViewSet):
    """
    **Albums API**

    Provides CRUD operations, filtering, search, and ordering capabilities
    for the music albums collection.

    - Filter by: `artist`, `title`, `year`, `genre`
    - Search across: `artist`, `title`, `year`, `genre`
    - Ordering: `year`, `artist`, `title`
    - Pagination: 20 items per page (default)
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
    search_fields = ["artist", "title", "year", "genre"]
    ordering_fields = ["year", "artist", "title"]
    ordering = ["id"]

    @extend_schema(
        summary="Get a random album",
        description="Return one random album from the database. "
        "If no albums exist, returns a 404 error.",
        responses={
            200: AlbumSerializer,
            404: OpenApiResponse(description="No albums found"),
        },
        examples=[
            OpenApiExample(
                "Random album response",
                value={
                    "id": 5,
                    "artist": "Fleetwood Mac",
                    "title": "Rumours",
                    "year": 1977,
                    "genre": "Rock",
                },
                response_only=True,
            ),
        ],
    )
    @action(detail=False, methods=["get"])
    def random(self, request):
        count = Album.objects.count()
        if count == 0:
            return Response(
                {"error": "No albums found"}, status=status.HTTP_404_NOT_FOUND
            )

        random_index = random.randint(0, count - 1)
        album = Album.objects.all()[random_index]
        serializer = self.get_serializer(album)
        return Response(serializer.data)
