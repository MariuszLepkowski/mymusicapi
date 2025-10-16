from django_filters import rest_framework as filters

from .models import Album


class AlbumFilter(filters.FilterSet):
    artist = filters.CharFilter(lookup_expr="icontains")
    title = filters.CharFilter(lookup_expr="icontains")
    genre = filters.CharFilter(lookup_expr="icontains")

    year__gte = filters.NumberFilter(field_name="year", lookup_expr="gte")
    year__lte = filters.NumberFilter(field_name="year", lookup_expr="lte")

    class Meta:
        model = Album
        fields = ["artist", "title", "genre", "year__gte", "year__lte"]
