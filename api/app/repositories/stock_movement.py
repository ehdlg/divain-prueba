from app.db.models import StockMovement
from sqlmodel import Session, select


class StockMovementRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, stock_movement: StockMovement):
        self.session.add(stock_movement)

        self.session.commit()

        return stock_movement

    def get_all(self) -> list[StockMovement]:
        statement = select(StockMovement)

        stock_movements = self.session.exec(statement).all()

        return stock_movements
