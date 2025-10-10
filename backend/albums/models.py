from django.db import models


class Album(models.Model):
    """
    Model representing a music album.
    """

    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.IntegerField(max_length=30)
    genre = models.CharField(max_length=255)

    class Meta:
        ordering = ["year", "artist"]
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.year})"
