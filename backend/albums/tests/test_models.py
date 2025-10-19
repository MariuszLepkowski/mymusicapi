import pytest


@pytest.mark.django_db
def test_album_str_representation(album_factory):
    album = album_factory(artist="Metallica", title="Ride the Lightning", year=1984)
    assert str(album) == "Metallica - Ride the Lightning (1984)"
