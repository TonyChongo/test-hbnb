
# HBnB Project

The **HBnB Project** is the second trimester web application project of Holberton School. It teaches students to design and implement a scalable web application using modern backend architectural practices.

Inspired by Airbnb, the project allows users to register, list properties, write reviews, and manage amenities. Built with Flask, it follows a layered architecture with clean separation of concerns.

---

## 🔧 Tech Stack

- **Backend Framework**: Flask (Python)
- **ORM / DB Layer**: SQLAlchemy (via custom DBStorage)
- **Database**: PostgreSQL (or SQLite for development)
- **Architecture**: Clean Architecture (Controllers → Facade → Models → Storage)
- **API Design**: RESTful
- **Documentation**: Markdown + UML diagrams

---

## 🧱 Project Structure

```
/hbnb/
├── controllers/       # API endpoints (Flask Blueprints)
├── services/          # Business logic
├── models/            # Entity classes (User, Place, Review, Amenity)
├── facade/            # Entry point for business operations
├── storage/           # DBStorage class using SQLAlchemy
├── static/            # Static assets (optional frontend)
├── config.py          # Configuration and environment
├── app.py             # Flask entry point
└── requirements.txt   # Dependencies
```

---

## 🚀 Getting Started

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/test-hbnb.git
cd test-hbnb/part2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set up Environment
Create a `.env` or use `config.py`:
```bash
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///hbnb.db
```

### 3. Run the App
```bash
flask run
```

---

## 📂 API Modules

- `/register`: User registration
- `/places`: Create, list, or filter places
- `/reviews`: Submit or view reviews
- `/amenities`: Manage amenities

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📄 Documentation

- **[HBnB_Technical_Architecture_Document.docx](./HBnB_Technical_Architecture_Document.docx)**  
  Includes:
  - Package Diagram
  - Class Diagram
  - Sequence Diagrams (Register, Place, Review, Filter)
  - Explanatory Notes

---

## 🧠 Design Principles

- **Facade Pattern**: Central point of entry to models and services
- **Service Layer**: Business logic separated from routing
- **Repository Pattern**: DB logic hidden behind `DBStorage`

---

## 🛠 TODO / Roadmap

- [x] User registration with validation
- [x] Place listing & creation
- [x] Submit and fetch reviews
- [ ] JWT-based authentication
- [ ] Admin dashboard (Flask-Admin or custom)
- [ ] Booking/payment module

---

## 🪪 License

MIT License. See `LICENSE`.
