import factory
from albums.models import Album


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    artist = factory.Faker("name")
    title = factory.Faker("sentence", nb_words=3)
    year = factory.Faker("year")
    genre = factory.Faker("word")
