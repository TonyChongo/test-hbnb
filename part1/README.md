
# HBnB - Part 01: System Architecture & Documentation (Flask)

This section is part of the second trimester project of Holberton School where students learn to build a full web application with clean architecture using Flask.

---

## 📘 What’s Included?

### ✅ Package Diagram
Outlines the three-layer architecture:
- **Presentation Layer**: Flask Controllers / Blueprints
- **Business Logic Layer**: Services and Facade
- **Persistence Layer**: DBStorage with SQLAlchemy

### ✅ Class Diagram
Visualizes core models:
- `User`, `Place`, `Review`, `Amenity` inherit from `BaseModel`
- Relationships (1:N, N:M) defined clearly

### ✅ Sequence Diagrams
Covers critical user flows:
- `POST /register`: Register user
- `POST /places`: Add a place
- `GET /places`: Search/filter places
- `POST /reviews`: Submit a review

---

## 📂 File: `HBnB_Technical_Architecture_Document.docx`

This document provides:
- Diagrams (Package, Class, Sequence)
- Explanations of components
- Architectural patterns used
- Rationale for each flow

---

## 📌 Usage

- Use this document as a blueprint before building new endpoints
- Onboard team members or contributors quickly
- Ensure that implementation aligns with architectural design

---

## 🧠 Patterns & Conventions

- **Facade Pattern** for decoupling layers
- **Service Layer** for complex business logic
- **Repository/DAO Layer** via `DBStorage`
- RESTful API design using Flask Blueprints

---

## ➕ What's Next?

Move to **Part 02: BL and API**
