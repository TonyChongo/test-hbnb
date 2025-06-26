
# 🏠 HBnB Project - Part 2: REST API, Models & Business Logic

## 📚 Overview

This project is a simplified **HBnB (Airbnb clone)** implemented using Python and Flask. It provides a **RESTful API** to manage `Users`, `Places`, `Amenities`, and `Reviews`. It follows a **clean architecture** using a **Facade (Business Logic Layer)** to separate domain models from HTTP logic.

---

## 🚀 Features

- Full CRUD for:
  - Users
  - Places
  - Reviews (including `DELETE`)
- Many-to-many support between `Places` and `Amenities`
- One-to-many between `Places` and `Reviews`
- Data validation (model-level)
- Swagger documentation with Flask-RESTx
- Full unit tests and manual tests (cURL/Swagger)

---

## 🧱 Project Structure

```
hbnb/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── amenities.py
│   ├── models/
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── amenities.py
│   │   ├── reviews.py
│   │   └── basemodel.py
│   ├── repositories/
│   │   └── memory_storage.py
│   ├── services/
│   │   └── facade.py
│   └── __init__.py
├── tests/
│   ├── test_users.py
│   ├── test_places.py
│   ├── test_reviews.py
├── run.py
├── README.md
└── requirements.txt
```

---

## 🧠 Core Concepts

### 🧩 Models

Each model inherits from `BaseModel`, providing an `id`, `created_at`, and `updated_at` by default.

- **User**: Represents the client or admin
- **Place**: Rental unit with geo and pricing info
- **Amenity**: Features available at a Place
- **Review**: Feedback and rating from a User on a Place

All models enforce **validation rules** like email format, price range, or string limits.

### 🔌 API Endpoints

#### `/api/v1/users`
- `GET /users`: list users
- `POST /users`: create user

#### `/api/v1/places`
- `GET /places`: list places
- `POST /places`: create place

#### `/api/v1/amenities`
- `GET /amenities`: list amenities
- `POST /amenities`: create amenity

#### `/api/v1/reviews`
- `GET /reviews`: list reviews
- `POST /reviews`: create review
- `PUT /reviews/<id>`: update review
- `DELETE /reviews/<id>`: delete review

#### `/api/v1/places/<place_id>/reviews`
- Get all reviews for a specific place

### 💼 Facade Pattern

All business logic and validation are centralized in `HBnBFacade` (`app/services/facade.py`). This ensures:

- Consistent validation
- Encapsulation of logic
- Simplified unit testing

Example methods:
```python
def create_user(self, data)
def create_place(self, data)
def get_all_reviews(self)
def delete_review(self, review_id)
```

---

## 🧪 Testing

### ✅ Manual Testing

All routes tested via:
- `cURL` (for edge cases)
- Swagger UI (`http://127.0.0.1:5000/api/v1/`)

### 🧪 Unit Testing

Run tests:
```bash
python3 -m unittest discover tests
```

All major functions (creation, error handling, retrieval) are tested for:
- Users
- Places
- Reviews

---

## ✅ Requirements

### Python Version

- `Python 3.10+` recommended

### Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the App

```bash
python3 run.py
```

App runs on: `http://127.0.0.1:5000`

---

## 🔍 Swagger Docs

Once app is running, visit:

```text
http://127.0.0.1:5000/api/v1/
```

You’ll find:
- Interactive UI
- Input schema definitions
- Try-out buttons for each endpoint

---

## ✅ Validations Summary

| Model   | Validation                                                                 |
|---------|----------------------------------------------------------------------------|
| User    | First/last name required, email format, email uniqueness                  |
| Place   | Title required, price > 0, valid latitude and longitude                   |
| Review  | Rating in 1–5, text required, linked user/place must exist                |
| Amenity | Name must not be empty                                                    |

---

## 📃 Example cURL

```bash
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Great stay!", "rating": 5, "user_id": "<uid>", "place_id": "<pid>"}'
```

---

## 👥 Contributors

- Chong Leang Ueng

---

## 📌 Notes

- Uses **in-memory storage** via `repositories/`.
- Ideal for testing or educational purposes.
- Future updates can include DB storage, auth, etc.

---
