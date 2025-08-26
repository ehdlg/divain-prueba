import random

from app.db.main import get_session_instance
from app.db.models import Product


def generate_sku(index: int) -> str:
    return f"SKU-{1000 + index}"


def generate_ean13() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(13))


def generate_product_name(index: int) -> str:
    return f"Test Product {index}"


def populate_products(num_products: int = 30):
    session = get_session_instance()

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
    session.commit()

    print(f"Inserted {len(products)} products into the database.")


if __name__ == "__main__":
    populate_products()
