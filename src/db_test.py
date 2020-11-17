from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import logging

import time
time.sleep(15)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

DB_USER = 'yugabyte'
DB_PASSWORD = 'yugabyte'
DATABASE = 'yugabyte'
DB_HOST = 'database'
DB_PORT = 5433

uri = 'postgresql+psycopg2://yugabyte:yugabyte@database:5433/yugabyte'
uri %= (DB_USER, 
        DB_PASSWORD, 
        DB_HOST, 
        DB_PORT, 
        DATABASE)

engine = create_engine(uri, echo=True)



Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)
Base.metadata.create_all(engine)


