from app.db.models import Product
from sqlmodel import Session, select


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Product)

        products = self.session.exec(statement).all()

        return products
