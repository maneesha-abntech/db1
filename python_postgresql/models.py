from sqlalchemy import Column, Integer, String
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    empid = Column(Integer, primary_key=True, index=True)
    empname = Column(String, index=True)
    emploc = Column(String, index=True)
    salary = Column(Integer, index=True)
    role = Column(String, index=True)
