# 🎵 mymusicapi

**mymusicapi** is a RESTful web service built with **Django REST Framework**, providing CRUD operations, filtering, and search functionality for a collection of music albums.
<div align="center">
<img src="docs/screenshots/swagger-docs.jpg" style="width:40%; height:auto; display: block; margin-left:auto; margin-right:auto;">
</div>

Designed as part of a **portfolio project**, this API demonstrates modern backend development practices — including containerization with Docker, automated testing, and CI with GitHub Actions.

---
## Prerequisites

Before running the project, make sure you have the following installed:

- **Docker** and **Docker Compose** (required)
- **Git** (for cloning the repository)
- (Optional) **Python 3.10+** — only if you want to run or inspect the code locally without Docker.

---

## Tech Stack

- **Python 3.12**
- **Django 5 / Django REST Framework**
- **PostgreSQL**
- **Docker & docker-compose**
- **Pytest + Factory Boy**
- **GitHub Actions** ([![CI](https://github.com/MariuszLepkowski/mymusicapi/actions/workflows/ci.yml/badge.svg)](https://github.com/MariuszLepkowski/mymusicapi/actions))
- **drf-spectacular** for automatic API documentation (Swagger / Redoc)
---
## API Documentation Preview

The API is fully documented using **drf-spectacular** and exposed through **Swagger** and **ReDoc**.

Once the containers are running, you can access:

- **Swagger →** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
<div align="center">
<img src="docs/screenshots/swagger-docs-example-1.jpg" style="width:90%; height:auto; display: block; margin-left:auto; margin-right:auto;">
</div>
<div align="center">
<img src="docs/screenshots/swagger-docs-example-2.jpg" style="width:90%; height:auto; display: block; margin-left:auto; margin-right:auto;">
</div>

- **ReDoc →** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)
<div align="center">
<img src="docs/screenshots/redoc-docs-example-1.jpg" style="width:90%; height:auto; display: block; margin-left:auto; margin-right:auto;">
</div>
<div align="center">
<img src="docs/screenshots/redoc-docs-example-2.jpg" style="width:900%; height:auto; display: block; margin-left:auto; margin-right:auto;">
</div>
<div align="center">
<img src="docs/screenshots/redoc-docs-example-3.jpg" style="width:80%; height:auto; display: block; margin-left:auto; margin-right:auto;">
</div>

You can also view the OpenAPI JSON schema directly:
[http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

---

## Installation & Setup

This project is fully containerized and runs via **Docker Compose**.
It includes a Django REST API backend and a PostgreSQL database service.

---

### Run the Application


### 1. Clone the repository
```sh
git clone https://github.com/MariuszLepkowski/mymusicapi
cd mymusicapi
```

### 2. Build and start the containers
```sh
docker-compose up --build
```
## After successful startup, visit:
- Albums API: http://localhost:8000/api/albums/
- Swagger UI: http://localhost:8000/api/docs/
- ReDoc documentation: http://localhost:8000/api/redoc/

#### To stop all containers:
```sh
docker-compose down
```
### 3. Set up environment variables

All environment variables are managed via the .env file.

Copy the example environment file and fill in your own keys:
```sh
cp .env.example .env
```
All environment variables are managed via the .env file.

Example:

    DJANGO_DEBUG=True
    POSTGRES_DB=mymusicapi
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

The docker-compose.yml file automatically provisions a PostgreSQL container and applies these settings.

### 4. Apply database migrations
Before using the API, make sure the database schema is created:
```sh
docker-compose exec web python manage.py migrate
```
This will apply all existing Django migrations and prepare the database tables.

### 5. Create a superuser (optional)
If you want to access the Django admin panel, create a superuser account:
```sh
docker-compose exec web python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.
Once created, visit:
- Django Admin: http://localhost:8000/admin/


### 6. Run Tests

You can run all tests inside the container:
```sh
docker-compose exec web pytest
```

Test results and coverage reports will be displayed in the console.


## Useful commands
```sh
# Rebuild containers (after code or dependency changes)
docker-compose up --build

# Apply database migrations
docker-compose exec web python manage.py migrate

# Access Django shell
docker-compose exec web python manage.py shell
```

## Try the API Yourself

You can quickly test the API locally using cURL.

**All example requests are provided in:**
[api_examples.md](api_examples.md)

Each example includes a ready-to-copy command and a sample JSON response.
No authentication required (Stage 1 demo API).

Example:
```sh
curl -X GET "http://localhost:8000/api/albums/?search=rock" \
     -H "Accept: application/json"
```

Response (example):
```sh
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "artist": "Pink Floyd",
      "title": "The Dark Side of the Moon",
      "year": 1973,
      "genre": "Progressive Rock"
    }
  ]
}
```
---

## Project Status

**Stage 1 – Completed**

The first milestone of the project is complete, focusing on the **Public Albums API** with the following features:
- Full CRUD operations (Create, Read, Update, Delete)
- Filtering, search, and ordering
- Pagination support
- Random album endpoint
- CSV-based data seeding
- Automated testing and continuous integration (GitHub Actions)
- OpenAPI documentation via Swagger & ReDoc

Currently, the project runs locally via Docker and is not yet deployed to production.
Deployment to a cloud environment (e.g. **AWS**, **Render**, or **DigitalOcean**) is planned for a later phase.

---

### Next Development Stages

#### Stage 2 – Authentication (JWT)
Add user authentication and authorization using **JSON Web Tokens (JWT)**.

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Log in and receive access + refresh tokens |
| `POST` | `/api/auth/refresh/` | Refresh access token |
| `GET` | `/api/auth/me/` | Retrieve data of the authenticated user |

---

#### Stage 3 – User Album Collection
Allow each authenticated user to manage their own private album collection.

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/me/albums/` | List albums in user’s collection |
| `POST` | `/api/me/albums/add/` | Add an album to user’s collection |
| `DELETE` | `/api/me/albums/{album_id}/` | Remove an album from collection |
| `PATCH` | `/api/me/albums/{album_id}/rating/` | Update rating / favorite status |

---

#### Stage 4 – Playlists
Enable users to create and manage personal playlists.

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/playlists/` | List all user playlists |
| `POST` | `/api/playlists/` | Create a new playlist |
| `GET` | `/api/playlists/{id}/` | Get playlist details (with albums) |
| `PATCH` | `/api/playlists/{id}/` | Edit playlist name or details |
| `DELETE` | `/api/playlists/{id}/` | Delete a playlist |
| `POST` | `/api/playlists/{id}/albums/add/` | Add an album to a playlist |
| `DELETE` | `/api/playlists/{id}/albums/{album_id}/` | Remove album from playlist |

---

#### Stage 5 – Recommendations
Add recommendation logic to suggest albums based on user preferences or favorite genres.

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/recommendations/` | Return recommended albums |

---

#### Stage 6 – User Statistics (Optional)
Provide data summaries and insights for each user.

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/stats/` | Returns summary data: total albums, top genres, playlists count, etc. |

---

### Summary

This repository represents the **first phase of a larger music collection API platform**.
It demonstrates clean REST architecture, Docker-based deployment, automated testing, and modern API documentation — serving as a portfolio project and a foundation for future feature expansion.


---
