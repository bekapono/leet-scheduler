import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

DB_URL = os.environ.get("DB_URL")

engine = create_engine(DB_URL)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()