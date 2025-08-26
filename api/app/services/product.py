from uuid import UUID

from app.db.models import StockMovement
from app.repositories.product import Product, ProductRepository
from app.repositories.stock_movement import StockMovementRepository
from pydantic import ValidationError


class ProductService:
    def __init__(
        self,
        product_reposistory: ProductRepository,
        stock_movement_repository: StockMovementRepository,
    ):
        self.product_repository = product_reposistory
        self.stock_repository = stock_movement_repository

    def get_all(self):
        products = self.product_repository.get_all()

        products = sorted(products, key=lambda p: p.sku)

        return products

    def get_one(self, id: UUID):
        return self.product_repository.get_one(id)

    def update(self, id: UUID, data: dict) -> Product:
        product = self.product_repository.get_one(id)

        if not product:
            raise ValueError(f"Product with id {id} not found.")

        if "stock" in data:
            self.__add_new_stock_movement(product, data)

        updated_product = self.product_repository.update(product, data)

        return updated_product

    def __add_new_stock_movement(self, product: Product, data: dict):
        new_stock = int(data["stock"])

        if new_stock < 0:
            raise ValidationError("Stock cannot be lesser than 0.")

        quantity = new_stock - product.stock

        if quantity == 0:
            return

        new_stock_movement = StockMovement(quantity=quantity, product_id=product.id)

        self.stock_repository.create(new_stock_movement)
