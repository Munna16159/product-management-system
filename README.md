#  Product CRUD API (FastAPI + SQLAlchemy)

A simple Product CRUD API built using FastAPI, SQLAlchemy, and environment-based configuration using `.env`.

---

## Features

* Create, Read, Update, Delete (CRUD) Products
* FastAPI backend
* SQLAlchemy ORM
* Environment variable management with `.env`
* SQLite / PostgreSQL support

---

## Tech Stack

* FastAPI
* SQLAlchemy
* Uvicorn
* Python-dotenv

---

## 📂 Project Structure

```
project/
│── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
│
│── .env
│── requirements.txt
│── README.md
```

---

## Setup Instructions

### 1 Clone the repository

```bash
git clone https://github.com/Munna16159/product-management-system.git
cd product-management-system
```

---

### 2 Create virtual environment

```bash
python -m venv venv
```

#### Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4 Create `.env` file

Create a `.env` file in the root directory:

```
DATABASE_URL=sqlite:///./test.db
```

For PostgreSQL:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

For MYSql:

```
DATABASE_URL=mysql+pymysql://fastapi_user:1234@localhost/fastapi_db
```
---

### 5 Run the application

```bash
uvicorn app.main:app --reload
```

---

### 6 How to Run Tests

Run this command from project root:

```
python -m unittest discover -s tests
```

This will automatically run all test files inside tests/

---

## API Docs

After running, open:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Example Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /products      | Get all products  |
| GET    | /products/{id} | Get product by ID |
| POST   | /products      | Create product    |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## Environment Variables

| Variable     | Description             |
| ------------ | ----------------------- |
| DATABASE_URL | Database connection URL |

---

## Requirements (example)

```
fastapi
uvicorn
sqlalchemy
python-dotenv
psycopg2-binary
```

---

## Notes

* Make sure `.env` is added to `.gitignore`

---
