# 🎬 Movie Reservation System — Backend (FastAPI)

A backend REST API for managing **movies**, **showtimes**, **users**, and **seat reservations**.  
Built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, structured using a clean architecture with services, routers, and tests.

---
## 🗄️ Database ERD (Entity Relationship Diagram)
This project uses a relational structure with Users, Roles, Movies, Showtimes, and Reservations.
Below is the full ERD showing table relationships:
![Database ERD](./docs/erd.png)


## ⚙️ Tech Stack

- **FastAPI** — Web framework  
- **SQLAlchemy ORM** — Database modeling  
- **PostgreSQL** — Main database  
- **Alembic** — Migrations  
- **Pydantic v2** — Data validation  
- **Pytest** — Unit & integration tests  
- **Uvicorn** — ASGI server  

---

## 📌 Features

### 🎞 Movies
- Full CRUD (Create, Read, Update, Delete)
- Pydantic validation
- Linked showtimes

### 🕒 Showtimes
- Each showtime belongs to a movie  
- Timezone-aware start times  
- Prevent past showtime creation  
- Pagination support  
- Cascade delete: removing a movie deletes its showtimes

### 💺 Reservations
- Dynamic seat generation based on hall capacity  
- Validate seat existence  
- Prevent double booking of a seat  
- Restrict cancellation for past showtimes

### 👤 Users & Authentication
- User model with password hashing  
- JWT authentication (login / register)  
- Role system (Admin / User) included  
- Users can only cancel their own reservations

### 🧪 Testing (unit + integration)
- SQLite in-memory testing setup  
- `tests/unit` for service logic  
- `tests/integration` for API-level behavior  
- `conftest.py` includes reusable test fixtures

---

## 📂 Project Structure

```bash
app/
├── core/ # Settings, config
├── models/ # SQLAlchemy ORM models
│ ├── movie.py
│ ├── showtime.py
│ ├── reservation.py
│ ├── user.py
│ └── role.py
├── routers/ # API endpoints (controllers)
│ ├── movies.py
│ ├── showtime.py
│ ├── reservation.py
│ └── auth.py
├── schemas/ # Pydantic models (request/response)
├── services/ # Business logic (service layer)
│ ├── auth_service.py
│ ├── movies_service.py
│ ├── reservation_service.py
│ ├── showtime_service.py
│ └── user_service.py
├── utils/ # Helpers (seat generation, DB setup)
│ ├── database.py
│ └── main.py
├── sql/ # Raw SQL or schema references
├── tests/ # Test suite
│ ├── unit/ # Unit tests (services)
│ ├── integration/ # Integration/API tests
│ └── conftest.py # Pytest fixtures
└── docs/
    └── erd.png # Database diagram
```
---

## 🚀 Run Locally

### 1️⃣ Clone the project
```bash
git clone https://github.com/azizsebri3/movie-reservation-system.git
cd movie-reservation-system/backend
python -m venv .venv
```
