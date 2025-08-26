import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Product(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    sku: str
    ean13: str
    stock: int = Field(default=0, ge=0)
    name: str

    movements: list["StockMovement"] = Relationship(back_populates="product")


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    name: str
    email: str

    movements: list["StockMovement"] = Relationship(back_populates="user")


class StockMovement(SQLModel, table=True):
    __tablename__ = "stock_movements"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    product_id: uuid.UUID = Field(foreign_key="product.id", nullable=False)
    quantity: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    user_id: Optional[uuid.UUID] = Field(default=None, foreign_key="user.id")

    product: Optional[Product] = Relationship(back_populates="movements")
    user: Optional[User] = Relationship(back_populates="movements")
