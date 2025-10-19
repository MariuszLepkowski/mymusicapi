import csv
import io

import pytest
from albums.models import Album
from django.core.management import call_command


@pytest.mark.django_db
def test_seed_csv_command_creates_albums(tmp_path):
    csv_path = tmp_path / "albums.csv"
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=["artist", "title", "year", "genre"]
        )
        writer.writeheader()
        writer.writerow(
            {
                "artist": "Tool",
                "title": "Lateralus",
                "year": 2001,
                "genre": "Progressive",
            }
        )
        writer.writerow(
            {
                "artist": "Kendrick Lamar",
                "title": "DAMN.",
                "year": 2017,
                "genre": "Hip-hop",
            }
        )

    out = io.StringIO()
    call_command("seed_csv", "--path", str(csv_path), stdout=out)

    assert "Seeded" in out.getvalue()
    assert Album.objects.count() == 2
