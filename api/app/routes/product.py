from uuid import UUID

from app.middlewares.main import ProductService, get_product_service
from app.routes.typings import UpdateProduct
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("")
async def get_products(
    product_service: ProductService = Depends(get_product_service),
):
    products = product_service.get_all()

    return products


@router.patch("/{id}")
async def update_product(
    id: UUID,
    product: UpdateProduct,
    product_service: ProductService = Depends(get_product_service),
):
    try:
        update_data = product.model_dump(mode="json", exclude_unset=True)

        updated_product = product_service.update(id, update_data)
    except ValueError:
        raise HTTPException(status_code=404, detail="Product not found")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

    return updated_product
