from typing import Optional

from pydantic import BaseModel


class UpdateProduct(BaseModel):
    sku: Optional[str] = None
    ean13: Optional[str] = None
    stock: Optional[int] = None
    name: Optional[str] = None
