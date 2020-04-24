
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

external_connection_string = 'postgresql://testuser:testpass@localhost:5430/testuser'
internal_connection_string = 'postgresql://testuser:testpass@localhost:5432/testuser'
engine = create_engine(external_connection_string)

Base = declarative_base()

Session = sessionmaker(bind=engine)
