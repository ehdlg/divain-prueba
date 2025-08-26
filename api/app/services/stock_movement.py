from app.db.models import StockMovement
from app.repositories.stock_movement import StockMovementRepository
from pydantic import ValidationError


class StockMovementService:
    def __init__(self, stock_movement_repo: StockMovementRepository):
        self.repository = stock_movement_repo

    def get_all(self):
        stock_moves = self.repository.get_all()

        stock_moves = [
            {
                **move.model_dump(mode="json"),
                "sku": move.product.sku,
                "ean13": move.product.ean13,
                "stock": move.product.stock,
            }
            for move in stock_moves
        ]

        return stock_moves

    def create(self, data: dict):
        try:
            stock_movement_instance = StockMovement(**data)

            return self.repository.create(stock_movement_instance)
        except ValidationError as e:
            print("Validation failed:", e)
            raise e
