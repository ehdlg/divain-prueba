from app.db.models import StockMovement
from app.repositories.stock_movement import StockMovementRepository
from pydantic import ValidationError


class StockMovementService:
    def __init__(self, stock_movement_repo: StockMovementRepository):
        self.repository = stock_movement_repo

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: dict):
        try:
            stock_movement_instance = StockMovement(**data)

            return self.repository.create(stock_movement_instance)
        except ValidationError as e:
            print("Validation failed:", e)
            raise e
