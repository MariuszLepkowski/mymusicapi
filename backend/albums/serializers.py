from albums.models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "artist", "title", "year", "genre"]
