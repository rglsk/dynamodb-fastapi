from uuid import UUID

from starlette import status
from starlette.testclient import TestClient

from app.repositories import ProductRepository
from app.schemas import ProductSchemaIn


def test_product_create(client: TestClient) -> None:
    data = {"name": "Book", "description": "A paper thing to read"}

    response = client.post("/v1/products", json=data)

    assert response.status_code == status.HTTP_201_CREATED

    response_data = response.json()
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert UUID(response_data["id"])
    assert isinstance(response_data["created_at"], int)
    assert isinstance(response_data["updated_at"], int)

    # check if product exists in db
    assert ProductRepository.get(response_data["id"])


def test_product_get(client: TestClient) -> None:
    product_in = ProductSchemaIn(name="Book", description="A paper thing to read")
    product = ProductRepository.create(product_in)

    response = client.get(f"/v1/products/{product.id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": str(product.id),
        "name": product.name,
        "description": product.description,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
    }
