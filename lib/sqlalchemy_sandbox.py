#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    # the engine is homebase for the database-everything on the db and python side must pass through the engine for the process to count
    engine = create_engine('sqlite:///students.db') 
    # create_all tells engine that any models created using base should be used to create tables
    Base.metadata.create_all(engine)