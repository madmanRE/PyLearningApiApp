from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_NAME, DB_PASSWORD

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_NAME}:{DB_PASSWORD}@localhost/pylearning"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
