from contextlib import contextmanager

from pymongo import MongoClient

MONGODB_URI = "mongodb://user:password@host:port/database"

_sessionmaker = None

# MongoDB connection string (replace with your actual connection string)
def initialize_mongodb_session_maker():
    global _sessionmaker
    if _sessionmaker is None:
        _sessionmaker = MongoClient(MONGODB_URI)
    return _sessionmaker

@contextmanager
def get_db():
    """
    Provides a context for accessing the MongoDB database.
    """
    session = initialize_mongodb_session_maker()
    try:
        yield session
    except Exception as e:
        session.close()
        raise e
    finally:
        session.close()