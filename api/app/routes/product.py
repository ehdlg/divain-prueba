from app.middlewares.main import ProductService, get_product_service
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("")
async def get_products(
    product_service: ProductService = Depends(get_product_service),
):
    products = product_service.get_all()

    return products
