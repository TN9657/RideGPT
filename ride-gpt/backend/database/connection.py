import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db_models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/ridegpt")

engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
        db.close()
    except Exception:
        yield None


def init_db():
    Base.metadata.create_all(bind=engine)
