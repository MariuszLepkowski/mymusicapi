## API Examples

This document provides **ready-to-use cURL** commands for testing the MyMusicAPI endpoints locally.

It’s intended as a quick reference for recruiters, reviewers, or developers exploring the project.

All endpoints are public (no authentication required in Stage 1).

#### Run your local server via Docker (http://localhost:8000) before executing the examples.

---
## 1. List all albums
```commandline
curl -X GET "http://localhost:8000/api/albums/" \
     -H "Accept: application/json"
```

Response:
```json
[
  {
    "id": 1,
    "artist": "Pink Floyd",
    "title": "The Dark Side of the Moon",
    "year": 1973,
    "genre": "Progressive Rock"
  },
  {
    "id": 2,
    "artist": "Radiohead",
    "title": "OK Computer",
    "year": 1997,
    "genre": "Alternative Rock"
  }
]

```
---
## 2. Filter or search albums
### Filter by artist:
```shell
curl -X GET "http://localhost:8000/api/albums/?artist=Radiohead" \
     -H "Accept: application/json"
```

### Search across all fields:
```shell
curl -X GET "http://localhost:8000/api/albums/?search=rock" \
     -H "Accept: application/json"
```

### Order by year (descending):
```shell
curl -X GET "http://localhost:8000/api/albums/?ordering=-year" \
     -H "Accept: application/json"
```

---
## 3. Retrieve single album by ID
```shell
curl -X GET "http://localhost:8000/api/albums/1/" \
     -H "Accept: application/json"
```

Response:
```json
{
  "id": 1,
  "artist": "Pink Floyd",
  "title": "The Dark Side of the Moon",
  "year": 1973,
  "genre": "Progressive Rock"
}
```

---
## 4. Create new album
```bash
curl -X POST "http://localhost:8000/api/albums/" \
     -H "Content-Type: application/json" \
     -d '{
           "artist": "Daft Punk",
           "title": "Random Access Memories",
           "year": 2013,
           "genre": "Electronic"
         }'
```

Response (201):
```json
{
  "id": 3,
  "artist": "Daft Punk",
  "title": "Random Access Memories",
  "year": 2013,
  "genre": "Electronic"
}
```
---
## 5. Update existing album
```bash
curl -X PUT "http://localhost:8000/api/albums/1/" \
     -H "Content-Type: application/json" \
     -d '{
           "artist": "Pink Floyd",
           "title": "Wish You Were Here",
           "year": 1975,
           "genre": "Progressive Rock"
         }'
```
Response:
```json
{
  "id": 1,
  "artist": "Pink Floyd",
  "title": "Wish You Were Here",
  "year": 1975,
  "genre": "Progressive Rock"
}
```
---
## 6. Partially update an album
```bash
curl -X PATCH "http://localhost:8000/api/albums/1/" \
     -H "Content-Type: application/json" \
     -d '{"genre": "Rock"}'
```
Response:
```json
{
  "id": 1,
  "artist": "Pink Floyd",
  "title": "The Dark Side of the Moon",
  "year": 1973,
  "genre": "Rock"
}
```
---
## 7. Delete album
```bash
curl -X DELETE "http://localhost:8000/api/albums/3/"
```
Response:
```json
204 No Content
```
---
## 8. Get a random album
```bash
curl -X GET "http://localhost:8000/api/albums/random/" \
     -H "Accept: application/json"
```
Response:
```json
{
  "id": 5,
  "artist": "Fleetwood Mac",
  "title": "Rumours",
  "year": 1977,
  "genre": "Rock"
}
```
---
