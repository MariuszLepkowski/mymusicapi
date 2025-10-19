import pytest
from albums.models import Album
from albums.tests.factories import AlbumFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAlbumAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.list_url = reverse("album-list")
        self.random_url = reverse("album-random")

    def test_list_albums(self):
        AlbumFactory.create_batch(3)
        response = self.client.get(self.list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3

    def test_create_album(self):
        payload = {
            "artist": "Radiohead",
            "title": "OK Computer",
            "year": "1997",
            "genre": "Rock",
        }
        response = self.client.post(self.list_url, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Album.objects.count() == 1
        assert Album.objects.first().artist == "Radiohead"

    def test_retrieve_album(self):
        album = AlbumFactory()
        url = reverse("album-detail", args=[album.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == album.id

    def test_update_album(self):
        album = AlbumFactory(artist="The Beatles")
        url = reverse("album-detail", args=[album.id])
        payload = {"artist": "The Rolling Stones"}
        response = self.client.patch(url, payload, format="json")
        assert response.status_code == status.HTTP_200_OK
        album.refresh_from_db()
        assert album.artist == "The Rolling Stones"

    def test_delete_album(self):
        album = AlbumFactory()
        url = reverse("album-detail", args=[album.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Album.objects.count() == 0

    def test_random_album(self):
        AlbumFactory.create_batch(5)
        response = self.client.get(self.random_url)
        assert response.status_code == status.HTTP_200_OK
        assert "artist" in response.data
        assert "title" in response.data
