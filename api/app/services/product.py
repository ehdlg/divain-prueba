from uuid import UUID

from app.repositories.product import Product, ProductRepository


class ProductService:
    def __init__(self, product_reposistory: ProductRepository):
        self.repository = product_reposistory

    def get_all(self):
        return self.repository.get_all()

    def get_one(self, id: UUID):
        return self.repository.get_one(id)

    def update(self, id: UUID, data: dict) -> Product:
        product = self.repository.get_one(id)

        if not product:
            raise ValueError(f"Product with id {id} not found.")

        updated_product = self.repository.update(product, data)

        return updated_product
