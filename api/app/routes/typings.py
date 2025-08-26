from typing import Optional

from pydantic import BaseModel, field_validator


class UpdateProduct(BaseModel):
    sku: Optional[str] = None
    ean13: Optional[str] = None
    stock: Optional[int] = None
    name: Optional[str] = None

    @field_validator("stock")
    def stock_must_be_non_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("Stock cannot be less than 0")

        return v
