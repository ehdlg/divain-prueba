from app.middlewares.main import StockMovementService, get_stock_movement_service
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("")
async def get_stock_movements(
    service: StockMovementService = Depends(get_stock_movement_service),
):
    moves = service.get_all()

    return moves
