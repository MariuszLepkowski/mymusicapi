from albums import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"albums", views.AlbumViewSet, basename="album")

urlpatterns = [
    path("", include(router.urls)),
]
