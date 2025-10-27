from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from . import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("albums.urls")),
    path("", include(schema.urlpatterns)),
]


if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
