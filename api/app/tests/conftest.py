import datetime
import random

import pytest
from app.db.main import get_session_instance
from app.db.models import Product, StockMovement
from app.db.populate_db import generate_ean13, generate_product_name, generate_sku
from sqlmodel import Session


@pytest.fixture(name="session")
def session_fixture():
    session = get_session_instance()
    try:
        yield session
    finally:
        session.rollback()

        session.close()


@pytest.fixture(name="products_fixture")
def products_fixture(session: Session):
    num_products = 10

    products = [
        Product(
            sku=generate_sku(i),
            ean13=generate_ean13(),
            stock=random.randint(0, 500),
            name=generate_product_name(i),
        )
        for i in range(1, num_products + 1)
    ]

    session.add_all(products)

    return products


@pytest.fixture(name="product")
def product_fixture(session: Session) -> Product:
    product = Product(
        sku=generate_sku(1),
        ean13=generate_ean13(),
        stock=random.randint(0, 500),
        name=generate_product_name(1),
    )

    session.add(product)

    return product


@pytest.fixture(name="stock_movements_fixture")
def stock_movements_fixture(session, products_fixture: list[Product]):
    movements = []

    for product in products_fixture:
        # Create a random number of movements for each product
        num_movements = random.randint(1, 5)
        for _ in range(num_movements):
            movement = StockMovement(
                product_id=product.id,
                quantity=random.randint(-50, 50),  # stock change
                timestamp=datetime.datetime.utcnow(),
                user_id=None,  # or assign a test user if you have one
            )
            movements.append(movement)

    session.add_all(movements)
