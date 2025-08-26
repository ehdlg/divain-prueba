from app.db.main import Session, get_session
from app.repositories.product import ProductRepository
from app.repositories.stock_movement import StockMovementRepository
from app.services.product import ProductService
from app.services.stock_movement import StockMovementService
from fastapi import Depends


async def get_product_repository(session: Session = Depends(get_session)):
    return ProductRepository(session)


async def get_stock_movements_repository(session: Session = Depends(get_session)):
    return StockMovementRepository(session)


async def get_product_service(
    product_repository: ProductRepository = Depends(get_product_repository),
):
    return ProductService(product_repository)


async def get_stock_movement_service(
    stock_movement_repository: StockMovementRepository = Depends(
        get_stock_movements_repository
    ),
):
    return StockMovementService(stock_movement_repository)
