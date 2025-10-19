import factory
from albums.models import Album
from faker import Faker

fake = Faker()


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    artist = factory.Faker("name")
    title = factory.Faker("sentence", nb_words=3)
    year = factory.LazyFunction(lambda: int(fake.year()))
    genre = factory.Faker("word")
