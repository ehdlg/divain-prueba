from uuid import UUID

from app.db.models import Product
from sqlmodel import Session, select


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Product]:
        statement = select(Product)

        products = self.session.exec(statement).all()

        return products

    def get_one(self, id: UUID | str) -> Product | None:
        if isinstance(id, str):
            id = UUID(id)

        statement = select(Product).where(Product.id == id)
        product = self.session.exec(statement).one_or_none()

        return product

    def update(self, product: Product, data: dict) -> Product:
        product.sqlmodel_update(data)

        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)

        return product
