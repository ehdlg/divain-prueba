from app.db.main import Session, get_session
from app.repositories.product import ProductRepository
from app.services.product import ProductService
from fastapi import Depends


async def get_product_repository(session: Session = Depends(get_session)):
    return ProductRepository(session)


async def get_product_service(
    product_repository: ProductRepository = Depends(get_product_repository),
):
    return ProductService(product_repository)
