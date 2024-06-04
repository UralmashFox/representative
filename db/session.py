from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from shopping.config import settings


SQLALCHEMY_DATABASE_URL = settings.DB_CONN_URI
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()