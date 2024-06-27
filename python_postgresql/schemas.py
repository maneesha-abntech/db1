# app/schemas.py
from pydantic import BaseModel

class EmployeeBase(BaseModel):
    empname: str
    emploc: str
    salary: int
    role: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    empid: int

    class Config:
        orm_mode = True
