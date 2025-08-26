from app.db.main import Session, get_session
from app.repositories.product import ProductRepository
from fastapi import Depends


async def get_product_repository(session: Session = Depends(get_session)):
    return ProductRepository(session)
