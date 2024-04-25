from sqlalchemy import create_engine, Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = 5432
DATABASE = 'company'
USER = 'postgres'
PASSWORD = 'nat2nat'

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'

    departmentid = Column("departmentid", Integer, primary_key=True, autoincrement=True)
    departmentname = Column("departmentname", String(30))

class Employees(Base):
    __tablename__ = 'employees'

    employeeid = Column("employeeid", Integer, primary_key=True, autoincrement=True)
    fullname = Column("fullname", String(40))
    hiredate = Column("hiredate", DateTime)
    departmentid = Column("departmentid", Integer, ForeignKey('departments.departmentid'))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

