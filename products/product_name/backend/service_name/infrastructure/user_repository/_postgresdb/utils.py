from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://user:password@host:port/database"

_sessionmaker = None

def initialize_session_maker():
    global _sessionmaker

    if _sessionmaker is None:
        engine = create_engine(DATABASE_URL)
        _sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return _sessionmaker

@contextmanager
def get_session() -> Session:
    """
    Provides a transactional scope around a series of operations.
    The session is automatically created and closed for you.
    """
    session = initialize_session_maker()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
