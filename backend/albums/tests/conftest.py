import pytest
from rest_framework.test import APIClient

from .factories import AlbumFactory


@pytest.fixture
def api_client():
    """DRF client for testing endpoints."""
    return APIClient()


@pytest.fixture
def album_factory():
    """Creates albums for tests."""
    return AlbumFactory
