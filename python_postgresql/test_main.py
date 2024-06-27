# test_main.py

from fastapi.testclient import TestClient
from main import app
from main import app, get_db  # Importing the get_db function

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base

# Connection URL for your PostgreSQL database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost/postgres"

# Create a test database session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees/", json={"empname": "John Doe", "emploc": "New York", "salary": 50000, "role": "Developer"})
    assert response.status_code == 200
    data = response.json()
    assert data["empname"] == "John Doe"
    assert data["emploc"] == "New York"
    assert data["salary"] == 50000
    assert data["role"] == "Developer"

def test_read_employee():
    response = client.get("/employees/1")
    assert response.status_code == 200
    data = response.json()
    assert data["empid"] == 1

def test_update_employee():
    response = client.put("/employees/1", json={"empname": "Jane Doe"})
    assert response.status_code == 200
    data = response.json()
    assert data["empname"] == "Jane Doe"

def test_delete_employee():
    response = client.delete("/employees/1")
    assert response.status_code == 200
    data = response.json()
    assert data["empid"] == 1
