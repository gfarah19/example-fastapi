from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from .config import settings


#this starts the db initially

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#this is for connecting to the database in a loop on startup until it's successful
#while True:
 #    try:
  #        conn = psycopg2.connect("host='localhost' dbname='fastapi' user='postgres' password='Skaana123!'")
   #       cursor = conn.cursor()
    #      print("Database connection was successful")
     #     break
     #except Exception as error:
      #    print("Connecting to database failed")
       #   print("Error: ", error)
        #  time.sleep(2)