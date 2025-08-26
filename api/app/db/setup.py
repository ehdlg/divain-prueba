from app.db.main import engine
from app.db.models import Product, StockMovement, User  # noqa: F401
from sqlmodel import SQLModel


def create_db_and_tables():
    try:
        engine.echo = False

        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)

        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    create_db_and_tables()
