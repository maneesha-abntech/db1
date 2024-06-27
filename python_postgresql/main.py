# main.py 
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
 
app = FastAPI()
 
models.Base.metadata.create_all(bind=engine)
 
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/{emp_id}", response_model=schemas.Employee)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.empid == emp_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    print( employee.empid, employee.empname, employee.emploc, employee.salary, employee.role)
    return employee

@app.put("/employees/{emp_id}", response_model=schemas.Employee)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.empid == emp_id).first()
    if db_employee:
        for attr, value in employee.dict().items():
            setattr(db_employee, attr, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

@app.delete("/employees/{emp_id}", response_model=schemas.Employee)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.empid == emp_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    return employee