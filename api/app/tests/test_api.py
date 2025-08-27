import pytest
from app.db.main import get_session
from app.db.models import Product, User
from app.main import app
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    client = TestClient(app)
    user = User(name="enrique", email="enriqueh147@gmail.com")

    app.dependency_overrides[get_session] = lambda: session

    session.add(user)

    yield client


@pytest.fixture(name="invalid_update_data")
def invalid_update_data_fixture():
    update_data = {"stock": -20}

    return update_data


@pytest.fixture(name="valid_update_data")
def valid_update_data_fixture():
    update_data = {"stock": 20}

    return update_data


def test_root_endpoint_works(client: TestClient, session: Session):
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK


def test_get_product_endpoint_should_return_a_list_of_products(
    client: TestClient, products_fixture
):
    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    product = data[0]

    assert "ean13" in product
    assert "sku" in product


def test_update_product_with_negative_stock_should_return_422_unprocessable_entity(
    client: TestClient, product: Product, invalid_update_data: dict
):
    response = client.patch(f"/products/{product.id}", json=invalid_update_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_update_product_with_valid_stock_should_update_the_stock(
    client: TestClient, product: Product, valid_update_data: dict
):
    response = client.patch(f"/products/{product.id}", json=valid_update_data)

    assert response.status_code == 200

    product = response.json()

    assert "stock" in product
    assert product["stock"] == valid_update_data["stock"]


def test_stock_movement_get_endpoint_should_return_a_list_of_stock_movements(
    client: TestClient, stock_movements_fixture
):
    response = client.get("/stock")

    assert response.status_code == 200

    stock_movements = response.json()

    assert isinstance(stock_movements, list)
    assert len(stock_movements) > 0

    stock_movement = stock_movements[0]

    assert "product_id" in stock_movement
    assert "quantity" in stock_movement
