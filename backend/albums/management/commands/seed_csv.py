import os
from csv import DictReader

from albums.models import Album
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Imports album data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            help="Optional: path to the CSV file (default: <BASE_DIR>/data/albums.csv)",
        )

    def handle(self, *args, **options):
        csv_path = options["path"] or os.path.join(
            settings.BASE_DIR, "..", "data", "albums.csv"
        )

        if not os.path.exists(csv_path):
            self.stderr.write(self.style.ERROR(f"File not found: {csv_path}"))
            return

        with open(csv_path, mode="r") as file:
            reader = DictReader(file)
            albums = []

            for row in reader:
                artist = row.get("artist")
                title = row.get("title")
                year = row.get("year")
                genre = row.get("genre")

                if not artist or not title:
                    self.stderr.write(
                        self.style.WARNING(f"Skipping incomplete row: {row}")
                    )
                    continue

                albums.append(
                    Album(
                        artist=artist.strip(),
                        title=title.strip(),
                        year=year.strip() if year else None,
                        genre=genre.strip() if genre else "",
                    )
                )

            Album.objects.bulk_create(albums, ignore_conflicts=True)

        self.stdout.write(
            self.style.SUCCESS(f"Seeded {len(albums)} albums successfully!")
        )
