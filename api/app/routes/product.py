from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_products():
    products = [f"product {i}" for i in range(10)]

    return products
