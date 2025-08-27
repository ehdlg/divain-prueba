import sys

from app.config import DATABASE_URL
from sqlmodel import Session, create_engine

if not DATABASE_URL:
    print("Error: DATABASE_URL not set.")

    sys.exit(1)

try:
    engine = create_engine(DATABASE_URL, echo=False)
except Exception as e:
    print(f"Failed to create engine: {e}")

    sys.exit(1)


def get_session():
    with Session(engine) as session:
        yield session


def get_session_instance():
    return Session(engine)
