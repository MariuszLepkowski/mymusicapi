from albums.models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    artist = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    genre = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Album` instance, given the validated data.
        """
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Album` instance, given the validated data.
        """
        instance.artist = validated_data.get("artist", instance.artist)
        instance.title = validated_data.get("title", instance.title)
        instance.year = validated_data.get("year", instance.year)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.save()
        return instance
