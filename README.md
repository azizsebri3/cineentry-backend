# 🎬 Movie Reservation System (Backend)

> Backend REST API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** — currently under active development as part of my backend learning roadmap.

---

## 🚀 Overview

This project is a **backend service** for a Movie Reservation System.  
It allows users to manage movies, showtimes, and (coming soon) seat reservations.  

I’m building it to **master backend engineering** concepts:
- CRUD operations with FastAPI  
- Database modeling with SQLAlchemy  
- Data validation using Pydantic v2  
- Relationships (One-to-Many, Many-to-One)  
- REST API design best practices  

---

🚀 Overview

This project is a backend service for a movie reservation system.
It allows users to manage movies, showtimes, and seat reservations (in progress).

I’m building it to master backend engineering concepts such as:

CRUD operations with FastAPI

Relational database modeling (SQLAlchemy ORM)

Data validation with Pydantic v2

One-to-Many and Many-to-Many relationships

Clean REST API design and error handling

---

## ⚙️ Tech Stack

| Layer         | Technology                            |
| ------------- | ------------------------------------- |
| Framework     | **FastAPI**                           |
| ORM           | **SQLAlchemy**                        |
| Database      | **PostgreSQL**                        |
| Validation    | **Pydantic v2**                       |
| Server        | **Uvicorn**                           |
| Documentation | **Swagger / OpenAPI**                 |
| Testing       | *(Coming soon)* pytest                |
| Deployment    | *(Planned)* Docker + Render / Railway |

---

## 📂 Current Features

### 🎞️ Movies
- Create, Read, Update, Delete movies  
- Schema-based validation  
- Clean error handling (404, validation, etc.)

### 🕒 Showtimes
- Linked to movies via `movie_id`  
- CRUD endpoints  
- Returns `movie_title` for each showtime  
- Pagination support (`skip`, `limit`)

### 💺 Reservation System

- Reservation model + service layer
- Seat generation and dynamic availability
- Validation and cancellation logic

---

## 🧱 Next Steps (in progress)

### 🔐 Authentication
- Implement JWT authentication  
- Add user roles (Admin / Customer)  
- Protect restricted routes  

### 🧰 DevOps
- Dockerize the app (FastAPI + Postgres)
- Unit tests with pytest  
- Deploy to Render / Railway  

---
🧩 Project Structure

app/
├── core/              # Config, constants, shared utils
├── routers/           # API routes
│   ├── movies.py
│   ├── showtime.py
│   └── reservation.py
├── services/          # Business logic separated from routers
│   ├── movie_service.py
│   ├── showtime_service.py
│   └── reservation_service.py
├── models/            # SQLAlchemy models
│   ├── movie.py
│   ├── showtime.py
│   └── reservation.py
├── schemas/           # Pydantic models for validation
│   ├── movie.py
│   ├── showtime.py
│   └── reservation.py
├── utils/             # Helpers (seat generation, etc.)
├── database.py        # Database engine and get_db()
└── main.py            # Application entrypoint


## 🧭 Learning Journey

This project is not finished yet — it evolves as I learn:
✅ FastAPI fundamentals
✅ SQLAlchemy relationships
✅ REST API design
🔜 Authentication and authorization
🔜 Database migrations and deployment

---

## 🧑‍💻 Setup (Local Development)

```bash
# Clone repository
git clone https://github.com/azizsebri3/movie-reservation-system.git
cd movie-reservation-system/backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

