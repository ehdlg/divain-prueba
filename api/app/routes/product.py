from app.middlewares.main import ProductRepository, get_product_repository
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("")
async def get_products(
    product_repo: ProductRepository = Depends(get_product_repository),
):
    products = product_repo.get_all()

    return products
