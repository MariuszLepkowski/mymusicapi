import pytest
from albums.serializers import AlbumSerializer


@pytest.mark.django_db
def test_album_serializer_output(album_factory):
    album = album_factory()
    serializer = AlbumSerializer(album)
    assert serializer.data["id"] == album.id
